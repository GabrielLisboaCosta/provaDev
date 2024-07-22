from django.urls import path
from consultas import views

app_name = 'consultas'

urlpatterns = [
    path('teste', views.teste),
    path('saudacao', views.saudacao),
    path('saudacao/<str:nome>', views.parametro),
    path('desafio/<str:nome>', views.desafio),
    path('paciente/read/<int:id>', views.paciente, name="read_paciente"),
    path('paciente', views.list_pacientes, name="pacientes"),
    path('atendimento/<int:id>', views.atendimento),
    # path('paciente/update/<int:paciente_id>', views.update, name="update_pacientes"),
    path('paciente/delete/<int:paciente_id>', views.delete, name="delete_pacientes"),
]
