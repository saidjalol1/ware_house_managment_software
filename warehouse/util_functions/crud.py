from django.utils.text import slugify

from django.http import JsonResponse, HttpResponse

# Create Product Object
def create_product(request, model):
    """Retrieve the fields of Objects"""
    category_id = request.POST.get("category")
    price = request.POST.get("price")
    size = request.POST.get("size")
    paint = request.POST.get("paint")
    currency = request.POST.get("currency")
    extra = request.POST.get("extra")
    
    if "add" in request.POST:
        object = model.objects.create(
            category_id = category_id,
            price = price,
            size = size,
            paint = paint,
            currency = currency,
            extra = extra
        )
        return object
    elif "edit" in request.POST:
        product = model.objects.get(id=request.POST.get("product"))
        product.price = request.POST.get("price")
        product.size = request.POST.get("size")
        product.paint = request.POST.get("paint")
        product.count = request.POST.get("count")
        product.currency = request.POST.get("currency")
        product.extra = request.POST.get("extra")
        product.save()
    else:
        pass
    


# Delete category Object
def delete_object(request,model):
    try:
        object = model.objects.get(id=request.POST.get("object"))
        print(object.paint)
        object.delete()
    except Exception as e:
        print(e, "Deleted")
    return {"Deleted"}


# Create Category Object
def create_category(request, model):
    """ Retrieve fields"""
    name = request.POST.get("name")
    
    slug = slugify(name)
    
    object = model.objects.create(
        name = name,
        slug= slug
    )
    
    return object

# Respons to ajax request
def edit_product(request, model):
    product_id = request.POST.get("product")
    product = model.objects.get(id=product_id)
    print(product.currency)
    if product:
        print(product)
        return JsonResponse({'success': True, 'product': {
                    'id': product.id,
                    'price': product.price,
                    'currency': product.currency,
                    'size': product.size,
                    'count': product.count,
                    'paint': product.paint,
                    'extra': product.extra,
                }})
    else:
        return JsonResponse({"success": False})
    
    
    
    