from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import serializers, models
from .pagination import Paginator

class ListCreateEventAPIView(generics.ListCreateAPIView):
    
    serializer_class = serializers.EventSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    pagination_class = Paginator

    def get_queryset(self):
        return models.Event.objects.all()
    

class UpdateEventAPIView(generics.RetrieveUpdateAPIView):
    
    serializer_class = serializers.BaseEventSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get_queryset(self):
        return models.Event.objects.all()
    
    
class DestroyEventAPIView(generics.RetrieveDestroyAPIView):
    
    serializer_class = serializers.BaseEventSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get_queryset(self):
        return models.Event.objects.all()
