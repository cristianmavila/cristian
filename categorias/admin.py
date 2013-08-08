# -*- coding: utf-8 -*-
from categorias.models import ItemCategoria
from django.contrib import admin
from django import forms
    
class CategoriaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Categoria', {'fields': ['nomecategoria']}),
    ]
    search_fields = ['nomecategoria']
    
admin.site.register(ItemCategoria, CategoriaAdmin)