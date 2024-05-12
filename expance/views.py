from django.shortcuts import render, redirect

from django.views import View
from .models import Expance

from .utils_func import _crud, pdf_print


class ExpanceView(View):
    template = "expance/expance.html"
    
    def get_context_data(self):
        context = {
            "objects" : Expance.objects.all()
        }
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template, context)
    
    def post(self, request):
        context = self.get_context_data()
        
        # search
        if "query" in request.POST:
            context["objects"] = Expance.objects.filter(name__icontains=request.POST.get("name"))
        # Date filter
        if "date_filter" in request.POST:
            start_date = request.POST.get("start_date")
            end_date = request.POST.get("end_date")
            context["objects"] = Expance.objects.filter(date_added__range = (start_date, end_date))
        # Create
        if "add" in request.POST:
            _crud.create_expance(request, Expance)
            return redirect("expance_app:expance_view")
        # Delete
        if "delete" in request.POST:
            object = Expance.objects.get(id=request.POST.get("object"))
            object.delete()
            return redirect("expance_app:expance_view")
        # Ajax response
        if "action_edit" in request.POST:
           return  _crud.edit_expance(request, Expance)
        # Edit
        if 'edit' in request.POST:
            _crud.create_expance(request, Expance)
            return redirect("expance_app:expance_view")
        # Pdf print
        if "pdf" in request.POST:
            return pdf_print.export_products_to_pdf(context["objects"])
        
        return render(request, self.template, context)
