from django.shortcuts import redirect
from django.urls import reverse_lazy
from ..models import Product, Category


def filter_by_date(request, model):
    start_date = request.POST.get("start_date")
    end_date = request.POST.get("end_date")
    if start_date and end_date:
        object = model.objects.filter(date_added__range=(start_date, end_date))
        return object
    else:
        return redirect("/")
    
    
def filter_by_name_category(request, model):
    slug = request.POST.get("slug")
    if slug:
        object = model.objects.filter(category__slug=slug)
        return object
    else:
        return redirect("/")
    

def filter_by_name(request, model):
    name = request.POST.get("name")
    if name:
        object = model.objects.filter(name__icontains=name)
        return object
    else:
        return redirect("/")
    
        