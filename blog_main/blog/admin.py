from django.contrib import admin
from .models import Category,Blogs
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','category','auther','featured_image','short_description','blog_body','status','is_featured','created_at','updated_at')
    list_filter = ('category','auther','status','is_featured')
    search_fields = ('title', 'category__category_name', 'auther__username', 'short_description', 'blog_body')#foreign key are represented as category__category_name
    prepopulated_fields={'slug':('title',)}
admin.site.register(Category)
admin.site.register(Blogs,BlogAdmin)
