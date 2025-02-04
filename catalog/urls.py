from django.urls import path
from mypy.types import names

from . import views
from .views import ProductListView,ContactTemplateView,ProductDetailView

app_name = 'catalog'

urlpatterns =[ path('', ProductListView.as_view(), name = 'product_list'),
               path('catalog/<int:pk>/', ProductDetailView.as_view(), name = 'products_detail'),
               path('contact/', ContactTemplateView.as_view(), name = 'contact_page')

]

# urlpatterns = [
#     path('home/', HomePageListView.as_view(), name = "home_page"),
#     path('contact/', ContactTemplateView.as_view(), name = 'contact_page'),
#     path('product_info/', views.product_info, name = 'product_info')
# ]