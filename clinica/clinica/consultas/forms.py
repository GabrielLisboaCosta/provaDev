from django.forms import ModelForm
from consultas.models.paciente import Paciente


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
