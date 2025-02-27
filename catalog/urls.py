from django.urls import path
from django.views.decorators.cache import cache_page
from . import views
from .views import ProductListView,ContactTemplateView,ProductDetailView

app_name = 'catalog'

urlpatterns =[ path('', ProductListView.as_view(), name = 'product_list'),
               path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name = 'products_detail'),
               path('contact/', ContactTemplateView.as_view(), name = 'contact_page'),
               path('catalog/create/', views.ProductCreateView.as_view(), name = 'product_create'),
               path('catalog/update/<int:pk>/', views.ProductUpdateView.as_view(), name = 'product_update'),
               path('catalog/delete/<int:pk>/', views.ProductDelete.as_view(), name = 'product_delete'),
               path('category/<int:pk>/', views.ProductsByCategoryView.as_view(), name='products_by_category')

]