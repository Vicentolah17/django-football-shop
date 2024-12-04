from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from camisa.models import Camisa
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from camisa.forms import FormularioCamisa

from camisa.serializers import SerializadorCamisa
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class CamisaViewSet(ModelViewSet):
    """
    API para realizar operações CRUD com Camisas
    """
    queryset = Camisa.objects.all()
    serializer_class = SerializadorCamisa
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ListarCamisas(LoginRequiredMixin, ListView):
    """
    View para listar camisas cadastradas.
    """
    
    model = Camisa
    context_object_name = 'camisas'
    template_name = 'camisa/listar.html'


class CriarCamisas(LoginRequiredMixin, CreateView):
    model = Camisa
    form_class = FormularioCamisa
    template_name = 'camisa/novo.html'
    success_url = reverse_lazy('listar-camisas')



class EditarCamisas(LoginRequiredMixin, UpdateView):
    model = Camisa
    form_class = FormularioCamisa
    template_name = 'camisa/editar.html'
    success_url = reverse_lazy('listar-camisas')


class DeletarCamisas(LoginRequiredMixin, DeleteView):
    model = Camisa
    template_name = 'camisa/deletar.html'
    success_url = reverse_lazy('listar-camisas')


class FotoCamisa(LoginRequiredMixin, View):
    def get(self, request, arquivo):
        try:
            camisa = Camisa.objects.get(foto='camisa/fotos/{}'.format(arquivo))
            return FileResponse(camisa.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não autorizado")
        except Exception as exception:
            raise exception
        



class APIListarCamisas(ListAPIView):
    '''
    View para listar instâncias de camisas (por meio do API REST)
    '''
    serializer_class = SerializadorCamisa
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Camisa.objects.all()
    

class APIDeletarCamisas(DestroyAPIView):
    """
    View para deletar instâncias de camisas (por meio da API REST)
    """
    serializer_class = SerializadorCamisa
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Camisa.objects.all()


class APICriarCamisas(CreateAPIView):
    """
    API para criar novas camisas.
    """
    serializer_class = SerializadorCamisa
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        serializer.save()


class APIEditarCamisas(UpdateAPIView):
    """
    API para editar camisas existentes.
    """
    serializer_class = SerializadorCamisa
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Camisa.objects.all()

    def perform_update(self, serializer):
        
        serializer.save()  
