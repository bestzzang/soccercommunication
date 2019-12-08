from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'cname','slug','category', 'pname', 'related_url', 'available_display','available_order','created','updated']
 #   list_display_links = ['related_url']
    list_filter = ['author', 'cname', 'pname', 'available_display','created','updated','category']
    prepopulated_fields = {'slug': ('cname', 'pname',)}
    raw_id_fields = ['author']
    search_fields = ['cname', 'pname', 'created']
    ordering = ['-updated', '-created']
    list_editable = ['cname','slug','category', 'pname', 'related_url', 'available_display','available_order']

admin.site.register(Product, ProductAdmin)