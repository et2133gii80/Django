from django.urls import path
from mypy.types import names

from blog.apps import BlogConfig
from . import views

app_name = BlogConfig.name

urlpatterns = [ path('blog/create/', views.BlogCreateView.as_view(), name= 'blog_create'),
                path('blog/', views.BlogListView.as_view(), name= 'blog_list'),
                path('blog/detail/<int:pk>/', views.BlogDetailView.as_view(), name= 'blog_detail')
]