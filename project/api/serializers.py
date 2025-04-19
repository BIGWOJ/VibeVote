from rest_framework import serializers
from .models import Room


# Serializers translates python code to JSON using Django Rest Framework
class Room_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'