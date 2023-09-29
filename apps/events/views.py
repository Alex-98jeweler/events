from django.db import IntegrityError
from rest_framework import decorators
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import serializers, models
from .pagination import Paginator

class ListCreateEventAPIView(generics.ListCreateAPIView):
    
    serializer_class = serializers.EventSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    pagination_class = Paginator

    def get_queryset(self):
        return models.Event.objects.all()
    

class UpdateEventAPIView(generics.RetrieveUpdateAPIView):
    
    serializer_class = serializers.BaseEventSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    
    def get_queryset(self):
        return models.Event.objects.all()
    
    
class DestroyEventAPIView(generics.RetrieveDestroyAPIView):
    
    serializer_class = serializers.BaseEventSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    
    def get_queryset(self):
        return models.Event.objects.all()


@decorators.api_view(http_method_names=['POST', ])
def follow_event(request, *args, **kwargs):
    event_id = kwargs.get('pk')
    user = request.user
    event = models.Event.objects.get(pk=event_id)
    try:
        models.EventFollower.objects.create(event=event, follower=user)
    except IntegrityError as e:
        return Response(data={'message': "You are already followed"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={'message': 'successfully followed'}, status=status.HTTP_200_OK)


@decorators.api_view(http_method_names=['POST', ])
@decorators.authentication_classes([JWTAuthentication, SessionAuthentication])
def unfollow_event(request, *args, **kwargs):
    event_id = kwargs.get('pk')
    user = request.user
    event = models.Event.objects.get(pk=event_id)
    try:
        event_follower = models.EventFollower.objects.get(event=event, follower=user)
        event_follower.delete()
    except Exception as e:
        return Response(data={'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={'message': 'successfully followed'}, status=status.HTTP_200_OK)


@decorators.api_view(('GET', ))
def get_followers(request, *args, **kwargs):
    event_id = kwargs.get('pk')
    followers = models.EventFollower.objects.filter(event_id=event_id).values('follower')
    return Response({"followers": list(followers)})

