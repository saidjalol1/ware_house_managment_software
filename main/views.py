from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View

from django.db.models import Count, Q, Sum, F

from sale.models import Sale
from warehouse.models import Product
from expance.models import Expance

from .models import *


class MainView(View):
    template = "main/index.html"
    
    def get_context_data(self, *args, **kwargs):
        current_month = datetime.now().month
        current_year = datetime.now().year
        
        current_month_sales = Sale.objects.filter(date_added__year=current_year, date_added__month=current_month)

        # Find the product ID of the most sold product for this month
        most_sold_product_id = current_month_sales.values('product').annotate(total_sold=Count('id')).order_by('-total_sold').first()['product']

        # Similar to previous, find the least sold product ID (excluding zero sales)
        least_sold_product_id = current_month_sales.filter(quantity__gt=0).values('product').annotate(total_sold=Count('id')).order_by('total_sold').first()['product']

        # Retrieve actual product objects
        most_sold_product = Product.objects.get(pk=most_sold_product_id)
        least_sold_product = Product.objects.get(pk=least_sold_product_id)

        # Calculate total sales amount for the current month
        total_sales_amount = current_month_sales.aggregate(total_amount=Sum(F('quantity') * F('product__price')))['total_amount']

        print(f"Total Sales for {current_month}/{current_year}:", total_sales_amount)
        
        context = {
            "objects" : Sale.objects.filter(status=False).filter(payment_type="nasiya"),
            "most_sold_product" : most_sold_product,
            "least_sold_product" : least_sold_product,
            "total_sales_amount" : total_sales_amount,
        }
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template, context)
    
    
    def post(self, request):
        context = self.get_context_data()
        if "pay" in request.POST:
            object = Sale.objects.get(id=request.POST.get("sale"))
            object.status = True
            object.save()
            print(object)
            return redirect("main:main_app")
        return render(request, self.template, context)