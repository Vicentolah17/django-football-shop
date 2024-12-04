from django.urls import path 
from camisa.views import ListarCamisas, FotoCamisa, CriarCamisas, EditarCamisas, DeletarCamisas, APIListarCamisas, APIDeletarCamisas, APIEditarCamisas,APICriarCamisas

urlpatterns = [ 
    path('', ListarCamisas.as_view(), name='listar-camisas'), 
    path('novo/', CriarCamisas.as_view(), name='criar-camisas'), 
    path('fotos/<str:arquivo>/', FotoCamisa.as_view(), name='foto-camisa'), 
    path('<int:pk>/', EditarCamisas.as_view(), name='editar-camisas'), 
    path('deletar/<int:pk>/', DeletarCamisas.as_view(), name='deletar-camisas'), 
    path('api/', APIListarCamisas.as_view(), name='api-listar-camisas'), 
    path('api/<int:pk>/', APIDeletarCamisas.as_view(), name='api-deletar-camisas'), 
    
    path('api/criar/', APICriarCamisas.as_view(), name='api-criar-camisa'),
    path('api/editar/<int:pk>', APIEditarCamisas.as_view(), name='api-editar-camisa'),
    

] 

