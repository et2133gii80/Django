from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','content', 'created_at', 'publication', 'number_views')
    search_fields = ('title',)
    list_filter = ('publication', 'created_at')