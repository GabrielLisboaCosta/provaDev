from rest_framework import viewsets
from django.contrib.auth.models import Group, User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from consultas.models import Paciente
from services.serializers import UserSerializer, GroupSerializer, PacienteSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite os métodos GET e POST
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite os métodos GET e POST
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite os métodos GET e POST
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


@api_view(['GET'])
def saudacao(request):
    return Response({"saudacao": "Boa noite DEV I!"})
