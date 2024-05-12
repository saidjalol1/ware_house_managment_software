from django.http import JsonResponse, HttpResponse
from warehouse.models import Product
from django.contrib import messages
# Create Product Object

def create_product(request, model):
    """Retrieve the fields of Objects"""
    name = request.POST.get("name")
    product_id = request.POST.get("product")
    quantity = request.POST.get("count")
    currency = request.POST.get("currency")
    payment_type = request.POST.get("payment_type")
    deadline = request.POST.get("deadline")
    extra = request.POST.get("extra")
    
    print(quantity)
    if "add" in request.POST:
        product = Product.objects.get(id=product_id)
        print(product.count)
        remainder = product.count - int(quantity)
        if remainder >= 0:
            object = model.objects.create(
                customer_name = name,
                product_id = product_id,
                quantity = quantity,
                currency = currency,
                payment_type = payment_type,
                deadline = deadline,
                extra = extra
            )
            product.count = remainder
            product.save()
        else:
            messages.warning(request, "Omborda bu Mahsulot yetarli emas")
        return object
    
    elif "edit" in request.POST:
        sale = model.objects.get(id=request.POST.get("product"))
        sale.customer_name = request.POST.get("name")
        sale.product = request.POST.get("product")
        sale.quantity = request.POST.get("quantity")
        sale.currency = request.POST.get("currency")
        sale.payment_type = request.POST.get("payment_type")
        sale.deadline = request.POST.get("deadline")
        sale.extra = request.POST.get("extra")
        sale.save()
    else:
        pass


# Respons to ajax request
def edit_product(request, model):
    sale_id = request.POST.get("sale_ob")
    sale = model.objects.get(id=sale_id)
    print(sale.currency)
    if sale:
        print(sale)
        return JsonResponse({'success': True, 'sale_ob': {
                    'id': sale.id,
                    'customer_name': sale.customer_name,
                    'currency': sale.currency,
                    'count': sale.quantity,
                    'payment_type': sale.payment_type,
                    'deadline': sale.deadline,
                    'extra': sale.extra,
                }})
    else:
        return JsonResponse({"success": False})
    
    
    
    