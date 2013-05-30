# -*- coding: utf-8 -*-
from portfolio.models import ItemPortfolio
from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor

class ItemPortfolioModelForm(forms.ModelForm):
    #texto = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = ItemPortfolio
        widgets = {
           'short_text': RedactorEditor(),
        }

class PortfolioAdmin(admin.ModelAdmin):
    form = ItemPortfolioModelForm
    #fieldsets = [
     #   ('Portfolio', {'fields': ['nome','texto']})
    #]
    #search_fields = ['nome']
    
admin.site.register(ItemPortfolio, PortfolioAdmin)