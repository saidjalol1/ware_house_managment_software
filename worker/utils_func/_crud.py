from django.http import JsonResponse
from warehouse.models import Category



def create_worker(request, model,type):
    if "add" in request.POST:
        if type == 'soatbay':
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            object = model.objects.create(
                name = name,
                surname = surname,
                type = "soatbay",
                per_hour = request.POST.get("per_hour"),
            )
            return object
        elif type == "ishbay":
            work = Category.objects.get(id=request.POST.get("work_type"))
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            
            object = model.objects.create(
                name = name,
                surname = surname,
                
                type = "ishbay",
                work_type = work
            )
        else:
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            object = model.objects.create(
                name = name,
                surname = surname,
                type = "oylik",
                salary = request.POST.get("salary"),
            )
    if "edit" in request.POST:
        edit_worker(request, model, type)


# To Edit the existing worker
def edit_worker(request, model, type):
    worker = model.objects.get(id=request.POST.get("worker"))
    print(worker)
    if type == "soatbay":
        worker.name = request.POST.get("name"),
        worker.surname = request.POST.get("surname"),
        worker.per_hour = request.POST.get("hourly")
        worker.save()
    elif type == "oylik":
        worker.name = request.POST.get("name"),
        worker.surname = request.POST.get("surname"),
        worker.salary = request.POST.get("salary")
        worker.save()
    else:
        work = Category.objects.get(id=request.POST.get("work_type"))
        worker.name = request.POST.get("name"),
        worker.surname = request.POST.get("surname"),
        worker.work_type = work
        worker.save()
    return worker

# Ajaz response to fill in the form
def edit_object(request, model, type):
    worker_id = request.POST.get("worker")
    worker = model.objects.get(id=worker_id)
    if worker:
        if type == "ishbay":
            return JsonResponse({'success': True, 'worker': {
                        'id': worker.id,
                        'name': worker.name,
                        'surname': worker.surname,
                        'work_type': worker.work_type.id,
                    }})
        elif type == "soatbay":
            return JsonResponse({'success': True, 'worker': {
                        'id': worker.id,
                        'name': worker.name,
                        'surname': worker.surname,
                        'per_hour': worker.per_hour,
                    }})
        else:
            return JsonResponse({'success': True, 'worker': {
                        'id': worker.id,
                        'name': worker.name,
                        'surname': worker.surname,
                        'salary': worker.salary,
                    }})
    else:
        return JsonResponse({"success": False})
    