from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import Room_Serializer


class Room_View(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = Room_Serializer
    