from django.urls import path
from consultas import views

app_name = 'consultas'

urlpatterns = [
    path('teste', views.teste),
    path('saudacao', views.saudacao),
    path('saudacao/<str:nome>', views.parametro),
    path('desafio/<str:nome>', views.desafio),
]
