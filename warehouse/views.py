from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import Category, Product



from .util_functions import object_filtering, crud, pdf_export_function

class WareHouseView(View):
    template = "warehouses/warehouse.html"
    
    def get_context_data(self, *args, **kwargs):
        context = {
            "category" : Category.objects.all(),
            "objects" : Product.objects.all(),
        }
        return context
    
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template, context)
    
    
    def post(self, request):
        context = self.get_context_data()
        
        # Delete
        if "delete_product" in request.POST:
            object = Product.objects.get(id=request.POST.get("object"))
            object.delete()
            return redirect("warehouse_app:warehouse")

        # Search 
        if "query" in request.POST:
            objects = object_filtering.filter_by_name(request,Product)
            context["objects"] = objects
        
        # Create
        if "add" in request.POST:
            try:
                object = crud.create_product(request, Product)
            except Exception as e:
                print(e)
                return redirect("warehouse_app:warehouse")
            
        if "edit" in request.POST:
            crud.create_product(request, Product)
            
        # Category Add
        if "addCategory" in request.POST:
            try:
                object = crud.create_category(request, Category)
            except Exception as e:
                print(e)
                return redirect("warehouse_app:warehouse")
            
        # Pdf Print
        if "pdf" in request.POST:
            return pdf_export_function.export_products_to_pdf(context["objects"])
            
        if "action_edit" in request.POST:
            return crud.edit_product(request, Product)
        return render(request, self.template, context)
    