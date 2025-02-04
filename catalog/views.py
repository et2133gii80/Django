from catalog.models import Product

from django.views.generic import ListView, DetailView, TemplateView



# Create your views here.
class ProductListView(ListView):
    model = Product


# def home_page(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'catalog/home.html', context = context)


class ProductDetailView(DetailView):
    model = Product

# def product_info(request):
#     product = Product.objects.get(id=7)
#     context = {
#         'product': product
#     }
#     return render(request, 'catalog/product_info.html', context = context)


class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"

# def contact_page(request):
#     return render(request, 'catalog/contact.html')


