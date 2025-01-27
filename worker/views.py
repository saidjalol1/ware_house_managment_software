from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.views import View

from .models import Worker, Attandance, Payments, WorkType
from warehouse.models import Category

from .utils_func import _crud

class WorkerView(View):
    template_name = "workers/workers_main.html"
    
    def get_context_data(self):
        context = {
            "works" : Category.objects.all(),
            "objects" : Worker.objects.filter(type="ishbay")
        }
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request):
        context = self.get_context_data()
        if "add" in request.POST:
            _crud.create_worker(request, Worker, "ishbay")
            return redirect("worker_app:worker_view")
        if "delete" in request.POST:
            worker = Worker.objects.get(id=request.POST.get("object"))
            worker.delete()
            return redirect("worker_app:worker_view")
        if "action_edit" in request.POST:
            return _crud.edit_object(request, Worker, "ishbay")
        if "edit" in request.POST:
            _crud.edit_worker(request, Worker, "ishbay")
            return redirect("worker_app:worker_view")
        return render(request, self.template_name, context) 
    

class WorkerMonth(View):
    template_name = "workers/monthly/monthly_workers.html"
    
    def get_context_data(self):
        context = {
            "works" : Category.objects.all(),
            "objects" : Worker.objects.filter(type="oylik")
        }
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request):
        context = self.get_context_data()
        if "add" in request.POST:
            _crud.create_worker(request, Worker, "oylik")
            return redirect("worker_app:worker_month")
        if "delete" in request.POST:
            worker = Worker.objects.get(id=request.POST.get("object"))
            worker.delete()
            return redirect("worker_app:worker_month")
        if "action_edit" in request.POST:
            return _crud.edit_object(request, Worker, "oylik")
        if "edit" in request.POST:
            _crud.edit_worker(request, Worker, "oylik")
            return redirect("worker_app:worker_month")
        return render(request, self.template_name, context) 
    

class WorkerHour(View):
    template_name = "workers/hourly/hourly_workers.html"
    
    def get_context_data(self):
        context = {
            "works" : Category.objects.all(),
            "objects" : Worker.objects.filter(type="soatbay")
        }
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request):
        context = self.get_context_data()
        if "add" in request.POST:
            _crud.create_worker(request, Worker, "soatbay")
            return redirect("worker_app:worker_hour")
        if "delete" in request.POST:
            worker = Worker.objects.get(id=request.POST.get("object"))
            worker.delete()
            return redirect("worker_app:worker_hour")
        if "action_edit" in request.POST:
            return _crud.edit_object(request, Worker, "soatbay")
        if "edit" in request.POST:
            _crud.edit_worker(request, Worker, "soatbay")
            return redirect("worker_app:worker_hour")
        return render(request, self.template_name, context) 


class WorkersHourDetail(View):
    template_name = "workers/hourly/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = {
            "object": Worker.objects.get(id=self.kwargs.get("pk"))
        }
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        redirect_url = reverse("worker_app:worker", kwargs={"pk" : self.kwargs["pk"]})
        if "add" in request.POST:
            leave = request.POST.get("leave"),
            paid = request.POST.get("paid")
            attand = Attandance.objects.create(
                worker = Worker.objects.get(id=self.kwargs["pk"]),
                come = request.POST.get("come"),
                )
            if leave:
                attand.leave = leave
            if paid:
                attand.paid = paid
            return render(request, self.template_name, context)
        if "delete" in request.POST:
            object = Attandance.objects.get(id=request.POST.get("object"))
            object.delete()
            return redirect(redirect_url)
        if "action_edit" in request.POST:
            object = request.POST.get("object")
            attan = Attandance.objects.get(id=object)
            come = attan.come
            leave = attan.leave
            paid = attan.paid
            if leave or paid or come:
                return JsonResponse({
                    "success": True, "object":{
                    "id" : attan.id,
                    'come':come,
                    'leave' :leave,
                    'paid' :paid,
                }
                })
        if "edit" in request.POST:
            object = Attandance.objects.get(id=request.POST.get("object"))
            come = request.POST.get("come")
            leave = request.POST.get("leave")
            paid = request.POST.get("paid")
            if come:
                object.come = come
            if leave:
                object.leave = leave
            if paid:
                object.paid = paid
            object.save()
            return redirect(redirect_url)
        return render(request, self.template_name, context)
    

class WorkersMonthDetail(View):
    template_name = "workers/monthly/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = {
            "object": Worker.objects.get(id=self.kwargs.get("pk"))
        }
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        redirect_url = reverse("worker_app:worker_detail_month", kwargs={"pk" : self.kwargs["pk"]})
        if "add" in request.POST:
            type = request.POST.get("type")
            amount = request.POST.get("amount")
            date = request.POST.get("date")
            payment = Payments.objects.create(
                worker = Worker.objects.get(id=self.kwargs["pk"]),
                amount = amount,
                date = date,
                type = type,
                )
            return render(request, self.template_name, context)
        if "delete" in request.POST:
            object = Payments.objects.get(id=request.POST.get("object"))
            object.delete()
            return redirect(redirect_url)
        if "action_edit" in request.POST:
            object = request.POST.get("object")
            payment = Payments.objects.get(id=object)
            return JsonResponse({
                    "success": True, "object":{
                    "id" : payment.id,
                    'amount':payment.amount,
                    'date' :payment.date,
                    'type' :payment.type,
                }
                })
        if "edit" in request.POST:
            object = Payments.objects.get(id=request.POST.get("object"))
            date = request.POST.get("date")
            type = request.POST.get("type")
            amount = request.POST.get("amount")
            if date:
                object.date = date
            if type:
                object.type = type
            if amount:
                object.amount = amount
            object.save()
            return redirect(redirect_url)
        return render(request, self.template_name, context)


class WorkersWorkDetail(View):
    template_name = "workers/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = {
            "works" : Category.objects.all(),
            "object": Worker.objects.get(id=self.kwargs.get("pk"))
        }
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        redirect_url = reverse("worker_app:worker_by", kwargs={"pk" : self.kwargs["pk"]})
        if "add" in request.POST:
            work = request.POST.get("work")
            amount = request.POST.get("amount")
            paid = request.POST.get("paid")
            payment = WorkType.objects.create(
                worker = Worker.objects.get(id=self.kwargs["pk"]),
                work_type = Category.objects.get(id=work),
                amount = amount,
                paid = paid,
                )
            return render(request, self.template_name, context)
        if "delete" in request.POST:
            object = WorkType.objects.get(id=request.POST.get("object"))
            object.delete()
            return redirect(redirect_url)
        if "action_edit" in request.POST:
            object = request.POST.get("object")
            payment = WorkType.objects.get(id=object)
            return JsonResponse({
                    "success": True, "object":{
                    "id" : payment.id,
                    'amount':payment.amount,
                    'work' :payment.work_type.id,
                    'paid' :payment.paid,
                }
                })
        if "edit" in request.POST:
            object = WorkType.objects.get(id=request.POST.get("object"))
            paid = request.POST.get("paid")
            work = request.POST.get("work")
            amount = request.POST.get("amount")
            if paid:
                object.paid = paid
            if amount:
                object.amount = amount
            if work:
                object.work_type = Category.objects.get(id=work)
            object.save()
            return redirect(redirect_url)
        return render(request, self.template_name, context)