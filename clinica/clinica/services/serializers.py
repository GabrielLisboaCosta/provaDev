from rest_framework import serializers
from django.contrib.auth.models import User, Group

from consultas.models import Paciente


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="services:user-detail")

    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email']


class GroupSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="services:group-detail")

    class Meta:
        model = Group
        fields = ['url', 'name']


class PacienteSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="services:paciente-detail")

    class Meta:
        model = Paciente
        fields = ['url', 'nome', 'cpf']
