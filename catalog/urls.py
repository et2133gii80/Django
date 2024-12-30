from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [path('home/', views.home_page, name = "home"),
               path('contact/', views.contact_page, name = 'contact')]