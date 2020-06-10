from django.contrib import admin
from core.models import Medicines

# Register your models here.

__author__ = 'Rodrigo.Oliveira'

@admin.register(Medicines)
class Medicines(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
