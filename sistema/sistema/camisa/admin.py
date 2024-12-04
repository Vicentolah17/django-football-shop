from django.contrib import admin
from camisa.models import Camisa


# Register your models here.
class CamisaAdmin(admin.ModelAdmin):
    list_display = ['id', 'marca', 'time', 'tipo', 'tamanho', 'foto']
    search_fields = ['time']

admin.site.register(Camisa, CamisaAdmin)  