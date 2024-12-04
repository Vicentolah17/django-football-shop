from django.db import models
from camisa.consts import *
from datetime import datetime

# Create your models here.
class Camisa(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCA)
    time = models.CharField(max_length=100)
    ano = models.IntegerField()
    tipo = models.SmallIntegerField(choices=OPCOES_TIPO)
    foto = models.ImageField(blank=True, null=True, upload_to='camisa/fotos')
    tamanho = models.SmallIntegerField(choices=OPCOES_TAMANHO)

    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(

            self.get_marca_display(),
            self.time,
            self.ano,
            self.get_tipo_display()
        )
    
    def anos_de_uso(self):
        return datetime.now().year - self.ano
    
    @property
    def camisa_novo(self):
        return self.ano == datetime.now().year