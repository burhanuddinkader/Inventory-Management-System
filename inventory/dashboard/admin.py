from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group,User 
# Register your models here.

admin.site.site_header="BKaderInventory"
class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'category','quantity')
    list_filter=['category']
admin.site.register(Product,ProductAdmin)
# admin.site.unregister(Group)