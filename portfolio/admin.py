# -*- coding: utf-8 -*-
from portfolio.models import ItemPortfolio,ItemPhotos
from django.contrib import admin
from django import forms
#from easy_thumbnails.fields import ThumbnailerImageField

#class PortfolioAdmin(admin.ModelAdmin):
    #form = ItemPortfolioModelForm
    #fieldsets = [
     #   ('Portfolio', {'fields': ['nome','texto']})
    #]
    #search_fields = ['nome']
    
    
class ItensInline(admin.StackedInline):
    model = ItemPhotos
    extra = 1

class PortfolioAdmin(admin.ModelAdmin):
    #form = ItemPortfolioModelForm
    fieldsets = [
        ('Portfolio', {'fields': ['nome','data','capa','urlsite','cliente','idcategoria','texto']}),
    ]
    inlines = [ItensInline]
    search_fields = ['nome']
    
admin.site.register(ItemPortfolio, PortfolioAdmin)