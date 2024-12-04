from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from camisa.models import Camisa
from camisa.forms import FormularioCamisa

from django.test import TestCase
from camisa.models import Camisa

from datetime import datetime
from django.test import TestCase
from camisa.models import Camisa

class CamisaTestCase(TestCase):
    def setUp(self):
        
        self.camisa1 = Camisa.objects.create(
            marca=1, 
            time="Time Azul",
            ano=2023,
            tipo=1,  
            tamanho=2  
        )
        self.camisa2 = Camisa.objects.create(
            marca=2,  
            time="Time Vermelho",
            ano=2022,
            tipo=2,  
            tamanho=3  
        )

    def test_camisa_time(self):
        
        self.assertEqual(self.camisa1.time, "Time Azul")
        self.assertEqual(self.camisa2.time, "Time Vermelho")

    def test_criar_nova_camisa(self):
        
        camisa = Camisa.objects.create(
            marca=3,  
            time="Time Preto",
            ano=2024,
            tipo=3,  
            tamanho=1  
        )
        self.assertEqual(camisa.time, "Time Preto")

    def test_lista_camisas(self):
        
        camisas = Camisa.objects.all()
        self.assertEqual(camisas.count(), 2)  


