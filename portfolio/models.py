# -*- coding: utf-8 -*-
from django.db import models
from django.forms import forms
from django import forms as forms
#from redactor.fields import RedactorField
from wysihtml5.fields import Wysihtml5TextField
from categorias.models import ItemCategoria
from clientes.models import ItemCli
from stdimage import StdImageField
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from django.template.defaultfilters import slugify

class ItemPortfolio(models.Model):
    nome = models.CharField(max_length=100,verbose_name=u'Nome do projeto')
    slug = models.SlugField(blank=True,max_length=200,unique=True)
    data = models.DateField(blank=False,verbose_name=u'Data do projeto')
    cliente = models.ForeignKey(ItemCli, verbose_name=u'Cliente')
    urlsite = models.URLField(verbose_name=u'URL do projeto',blank=True)
    texto = Wysihtml5TextField(verbose_name=u'Descrição',blank=True)
    capa = StdImageField(upload_to='uploads/thumbs/', blank=True, size=(294, 327))
    idcategoria = models.ManyToManyField(ItemCategoria,verbose_name=u'Categorias')
    
    def save(self):
        if not self.id:
            self.slug = slugify(self.nome)
        super(ItemPortfolio, self).save()
    
    class Meta:
         verbose_name = "Trabalho"
         verbose_name_plural = "Trabalhos"
         db_table = "tb_portfolio"
    
    
    def __unicode__(self):
        #return self.nome
        return "%s"% self.nome
    
class ItemPhotos(models.Model):
    idPort = models.ForeignKey(ItemPortfolio)
    #foto = StdImageField(upload_to='uploads/fullfotos/', blank=True, size=(1280, 914))
    foto = models.ImageField(upload_to='uploads/fullfotos/',blank=True)
    #foto = AjaxImageField(upload_to='uploads/fullfotos/',max_height=550,max_width=1050,crop=True)
    
    class Meta:
         verbose_name = "Foto"
         verbose_name_plural = "Fotos"
         db_table = "tb_fotos"
    
    def __unicode__(self):
        return self.foto.url
    
class FormContato(forms.Form):
    name = forms.CharField()
    mail = forms.EmailField()
    msg = forms.CharField(widget=Textarea())