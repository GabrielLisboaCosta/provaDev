from django.core.validators import MinLengthValidator
from django.db import models
from consultas.models.plano import Plano
from consultas.models.prioridade import Prioridade
from consultas.models import BaseModel, Paciente


class Atendimento(BaseModel):
    class Meta:
        abstract = False
    date = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    reconsulta = models.BooleanField()
    exames = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    encaminhamento = models.CharField(max_length=500, validators=[MinLengthValidator(10)])
    plano = models.CharField(max_length=20, choices=Plano, default=Plano.PUBLIC)
    prioridade = models.CharField(max_length=20, choices=Prioridade, default=Prioridade.LOW)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

