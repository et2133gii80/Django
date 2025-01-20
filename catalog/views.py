from catalog.models import Product
from django.shortcuts import render


# Create your views here.
def home_page(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalog/home.html', context = context)

def contact_page(request):
    return render(request, 'catalog/contact.html')

def product_info(request):
    product = Product.objects.get(id=7)
    context = {
        'product': product
    }
    return render(request, 'catalog/product_info.html', context = context)
