# -*- coding: utf-8 -*-
from django.db import models
from django.forms import forms
from redactor.fields import RedactorField

class ItemPortfolio(models.Model):
    nome = models.CharField(max_length=2,verbose_name=u'Nome projeto')
    texto = RedactorField(verbose_name=u'Text',redactor_options={'lang': 'pt_br', 'focus': 'true'},upload_to='tmp/')
    def __unicode__(self):
        return self.nome

