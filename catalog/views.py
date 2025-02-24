from itertools import product

from django.core.exceptions import PermissionDenied
from mypy.types import names

from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import ProductForm, ProductModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



# Create your views here.
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    #fields = '__all__'
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    #fields = '__all__'
    # form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        if self.request.user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        product = self.get_object()
        if product.owner_id == self.request.user.id:
            return ProductForm
        raise PermissionDenied



class ProductDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_anonymous:
            return qs.filter(status=True)
        if not self.request.user.groups.filter(name='product_moderator'):
            return qs.filter(status=True)
        return qs

class ProductDetailView(DetailView):
    model = Product

class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"
