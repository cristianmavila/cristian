from django.db import models

class ItemCategoria(models.Model):
    nomecategoria = models.CharField(max_length=200,verbose_name=u'Nome da categoria')
    
    class Meta:
         verbose_name = "Categoria"
         verbose_name_plural = "Categorias"
         db_table = "tb_categoria"
    
    def __unicode__(self):
        return self.nomecategoria
