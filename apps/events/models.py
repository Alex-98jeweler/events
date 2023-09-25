from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    
    title = models.CharField('Название', max_length=50, unique=True)
    description = models.CharField('Описание', max_length=512)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class EventFollower(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    follower = models.ForeignKey(User, models.SET_NULL, null=True)