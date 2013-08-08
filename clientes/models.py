from django.db import models

class ItemCli(models.Model):
    nomecliente = models.CharField(max_length=200,verbose_name=u'Nome do cliente')
    
    class Meta:
         verbose_name = "Cliente"
         verbose_name_plural = "Clientes"
         db_table = "tb_cliente"
    
    def __unicode__(self):
        return self.nomecliente
