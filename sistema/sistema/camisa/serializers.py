from rest_framework import serializers
from camisa.models import Camisa
from drf_extra_fields.fields import Base64ImageField

class SerializadorCamisa(serializers.ModelSerializer):
    '''
    Serializador para o model Camisa
    '''

    nome_marca = serializers.SerializerMethodField()
    nome_tipo = serializers.SerializerMethodField()
    nome_tamanho = serializers.SerializerMethodField()
    foto = Base64ImageField(required=False, represent_in_base64=True)
    
    class Meta:
        model = Camisa
        exclude = []


    def get_nome_marca(self, instacia):
        return instacia.get_marca_display()
    
    def get_nome_tipo(self, instacia):
        return instacia.get_tipo_display()
    
    def get_nome_tamanho(self, instacia):
        return instacia.get_tamanho_display()
    
