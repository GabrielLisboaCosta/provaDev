from django.urls import path
from rest_framework import routers

from services import views

app_name = 'services'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'grups', views.GroupViewSet)
router.register(r'pacientes', views.PacienteViewSet)

urlpatterns = [
    path('saudacao/', views.saudacao, name="saudacao"),
]

urlpatterns += router.urls
