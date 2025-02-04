from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
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

    def get_queryset(self):
        return Blog.objects.filter(publication=True)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object =super().get_object(queryset)
        self.object.number_views +=1
        self.object.save
        return self.object

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')
