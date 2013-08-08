# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea
from agenda.models import ItemPortfolio
    
class FormPortfolio(ModelForm):
     class Meta:
        model = ItemPortfolio
        fields = ('nome', 'texto')
        widgets = {
            'texto': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
    