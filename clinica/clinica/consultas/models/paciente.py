from django.core.validators import MinLengthValidator
from django.db import models

from clinica.consultas.models.base import BaseModel
from clinica.consultas.models.parentesco import Parentesco
from clinica.consultas.models.tipo_alergia import TipoAlergia


class Paciente(BaseModel):
    nome = models.CharField(max_length=100, validators=MinLengthValidator[10])
    cpf = models.CharField(max_length=11, validators=MinLengthValidator[11], unique=True)
    endereco = models.CharField(max_length=100, validators=MinLengthValidator[20])
    cidade = models.CharField(max_length=50, validators=MinLengthValidator[3])
    tipo_alergia = models.CharField(max_length=20, choices=TipoAlergia, default=TipoAlergia.FOOD)
    alergias = models.CharField(max_length=100, validators=MinLengthValidator[5], null=True, blank=True) #null e blank nulos obrigatorios
    telefone = models.CharField(max_length=20, validators=MinLengthValidator[10])
    tel_emergencia = models.CharField(max_length=20, validators=MinLengthValidator[10])
    nome_contato = models.CharField(max_length=100, validators=MinLengthValidator[10])
    parentesco = models.CharField(max_length=20, choices=Parentesco, default=Parentesco.OTHER)

    def __str__(self):
        return f'{self.nome} : {self.cpf}'

    def paciente_por_cpf(self, cpf_pesquisa: str):
        if isinstance(cpf_pesquisa, str):
            if len(cpf_pesquisa) == 11:
                return Paciente.objects.get(cpf=cpf_pesquisa)
            else:
                return ValueError("O cpf informado deve conter 11 digitos")
        else:
            raise TypeError("cpf n é str")
