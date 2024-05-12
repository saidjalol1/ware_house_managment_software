from django.http import JsonResponse, HttpResponse
from warehouse.models import Product
from django.contrib import messages
# Create Product Object

def create_expance(request, model):
    """Retrieve the fields of Objects"""
    name = request.POST.get("name")
    amount = request.POST.get("amount")
    currency = request.POST.get("currency")

    if "add" in request.POST:
        object = model.objects.create(
            name = name,
            amount = amount,
            currency = currency,
        )
        return object
    
    elif "edit" in request.POST:
        expance = model.objects.get(id=request.POST.get("expance"))
        expance.name = request.POST.get("name")
        expance.amount = request.POST.get("amount")
        expance.currency = request.POST.get("currency")
        expance.save()
    else:
        pass


# Respons to ajax request
def edit_expance(request, model):
    expance_id = request.POST.get("expance")
    expance = model.objects.get(id=expance_id)
    if expance:
        return JsonResponse({'success': True, 'expance': {
                    'id': expance.id,
                    'name': expance.name,
                    'amount': expance.amount,
                    'currency': expance.currency,
                }})
    else:
        return JsonResponse({"success": False})
    
    
    
    