from django.contrib import admin
from consultas.models import Paciente
from consultas.models import Atendimento

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Atendimento)
