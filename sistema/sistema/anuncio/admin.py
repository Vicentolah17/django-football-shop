from django.contrib import admin
from anuncio.models import Anuncio


# Register your models here.
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'descricao', 'camisa', 'usuario', 'preco']
    search_fields = ['descricao','camisa_time','usuario']

admin.site.register(Anuncio, AnuncioAdmin)