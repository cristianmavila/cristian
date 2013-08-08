# -*- coding: utf-8 -*-
from clientes.models import ItemCli
from django.contrib import admin
from django import forms
    
class CliAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Cliente', {'fields': ['nomecliente']}),
    ]
    search_fields = ['nomecliente']
    
admin.site.register(ItemCli, CliAdmin)