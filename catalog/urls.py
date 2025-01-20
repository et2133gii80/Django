from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home_page, name = "home_page"),
    path('contact/', views.contact_page, name = 'contact_page'),
    path('product_info/', views.product_info, name = 'product_info')
]