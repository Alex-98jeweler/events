from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from apps.custom_user.serializers import UserSerializer

class Event(models.Model):
    
    title = models.CharField('Название', max_length=50, unique=True)
    description = models.CharField('Описание', max_length=512)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    @property
    def followers(self):
        result = []
        event_followers = EventFollower.objects.filter(event=self)
        for follower in event_followers:
            data = UserSerializer(follower.follower)
            result.append(data.data)
        return result


class EventFollower(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        unique_together = [['event', 'follower'], ]