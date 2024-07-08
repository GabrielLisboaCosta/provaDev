from django.contrib import admin
from clinica.consultas.models import Paciente
from clinica.consultas.models import Atendimento

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Atendimento)
