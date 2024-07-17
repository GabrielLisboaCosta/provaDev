from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models

from consultas.models import Atendimento
from consultas.models.plano import Plano
from consultas.models.base import BaseModel
from consultas.models.parentesco import Parentesco
from consultas.models.tipo_alergia import TipoAlergia


class Paciente(BaseModel):
    class Meta:
        abstract = False
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)], unique=True)
    endereco = models.CharField(max_length=100, validators=[MinLengthValidator(20)])
    cidade = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    tipo_alergia = models.CharField(max_length=20, choices=TipoAlergia, default=TipoAlergia.FOOD)
    alergias = models.CharField(max_length=100, validators=[MinLengthValidator(5)], null=True, blank=True) #null e blank nulos obrigatorios
    telefone = models.CharField(max_length=20, validators=[MinLengthValidator(10)])
    tel_emergencia = models.CharField(max_length=20, validators=[MinLengthValidator(10)])
    nome_contato = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    parentesco = models.CharField(max_length=20, choices=Parentesco, default=Parentesco.OTHER)

    def __str__(self):
        return f'{self.nome} : {self.cpf}'

    def paciente_por_cpf(cpf_pesquisa: str):
        if isinstance(cpf_pesquisa, str):
            if len(cpf_pesquisa) == 11:
                if cpf_pesquisa.isnumeric():
                    return Paciente.objects.get(cpf=cpf_pesquisa)
                else:
                    return ValueError("Digite apenas números")
            else:
                return ValueError("O cpf informado deve conter 11 digitos")
        else:
            raise TypeError("cpf n é str")

    def pacientes_por_data_plano(date_pesquisa: date, plano_pesquisa: Plano):
        if isinstance(date_pesquisa, date):
            if isinstance(plano_pesquisa, Plano):
                return [Paciente.objects.filter(atendimento__date=date_pesquisa).filter(atendimento__plano=plano_pesquisa)]
            else:
                return TypeError("O dado informado não é do tipo plano")
        else:
            return TypeError("O dado informado não é do tipo Date")

    #não consigo testar
    def pacientes_por_alergia(alergia: tipo_alergia):
        if isinstance(alergia, TipoAlergia):
            return [Paciente.objects.get(tipo_alergia=alergia)]
        else:
            raise TypeError("O dado não corresponde a um tipo de alergia válido")
