from django.conf import settings
from django.http import HttpRequest
from rest_framework import authentication, exceptions
import jwt

from . import models

class JWTAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request: HttpRequest):
        token = request.COOKIES.get('jwt')
        if not token:
            return None
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
        except:
            raise exceptions.AuthenticationFailed("Unathorized")
        user = models.User.objects.get(id=payload['id'])
        return (user, None)