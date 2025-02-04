from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title','content','image']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'
