from django.shortcuts import render
from rest_framework import generics

from . import serializers, models


class ListCreateEventAPIView(generics.ListCreateAPIView):
    
    serializer_class = serializers.EventSerializers

    def get_queryset(self):
        return models.Event.objects.all()
    

class UpdateEventAPIView(generics.RetrieveUpdateAPIView):
    
    serializer_class = serializers.EventSerializers
    
    def get_queryset(self):
        return models.Event.objects.all()
    
    
class DestroyEventAPIView(generics.RetrieveDestroyAPIView):
    
    serializer_class = serializers.EventSerializers
    
    def get_queryset(self):
        return models.Event.objects.all()
