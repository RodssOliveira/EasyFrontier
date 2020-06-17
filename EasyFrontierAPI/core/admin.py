from django.contrib import admin
from core.models import Medicines, ProductType, Order

# Register your models here.

__author__ = 'Rodrigo.Oliveira'

@admin.register(Medicines)
class Medicines(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']

@admin.register(ProductType)
class ProductType(admin.ModelAdmin):
    list_display = ['id', 'status']
    search_fields = ['id', 'status']


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ['id', 'code']
    search_fields = ['id', 'code']
