from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


from .models import *


class MainView(View):
    template = "main/index.html"
    
    def get_context_data(self, *args, **kwargs):
        context = {}
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template, context)
    
    
    def post(self, request):
        context = self.get_context_data()
        return render(request, self.template, context)