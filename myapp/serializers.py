from rest_framework import serializers
from .models import ExampleModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= ExampleModel
        fields= '__all__'
