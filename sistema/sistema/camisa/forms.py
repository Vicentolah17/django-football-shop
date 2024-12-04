from django.forms import ModelForm
from camisa.models import Camisa


class FormularioCamisa(ModelForm):

    class Meta:
        model = Camisa
        exclude = []