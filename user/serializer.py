from rest_framework import serializers
from .models import *
from djoser.serializers import TokenCreateSerializer

class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = ['title']

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['title']

class ProfileSerializer(serializers.ModelSerializer):
    position = serializers.SlugRelatedField(slug_field='title', queryset=Position.objects.all())
    structure = serializers.SlugRelatedField(slug_field='title', queryset=Structure.objects.all())
    class Meta:
        model = Profile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password','fio']

