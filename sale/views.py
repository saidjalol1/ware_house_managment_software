from django.shortcuts import render, redirect
from django.views import View

from .models import Sale
from warehouse.models import Product

from .pdf_export_function import export_products_to_pdf
from .func_utils import _crud


class SaleView(View):
    template = "sale/sale.html"
    
    
    def get_context_data(self,*args,**kwargs):
        context = {
            "products" : Product.objects.filter(count__gt = 0),
            "objects" : Sale.objects.all()
        }
        return context
    
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template, context)
    
    
    def post(self, request): # Create
        context = self.get_context_data()
        
        # Create
        if "add" in request.POST:
            try:
                object = _crud.create_product(request, Sale)
                return redirect("sale_app:sale_view")
            except Exception as e:
                print(e)
                return redirect("sale_app:sale_view")
        
        if "delete_product" in request.POST:
            object = Sale.objects.get(id=request.POST.get("object"))
            object.delete()
            return redirect("sale_app:sale_view")
        
        if "edit" in request.POST:
            _crud.create_product(request, Sale)
            
        if "action_edit" in request.POST:
            return _crud.edit_product(request, Sale)
        
        if "pdf" in request.POST:
            return export_products_to_pdf(context["objects"])
        
        return render(request, self.template, context)
    