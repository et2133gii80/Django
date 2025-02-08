from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import ProductForm



# Create your views here.
class ProductCreateView(CreateView):
    model = Product
    #fields = '__all__'
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    #fields = '__all__'
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductDelete(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"


