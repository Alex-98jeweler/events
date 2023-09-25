from rest_framework import views, response, exceptions, permissions
from rest_framework.request import Request

from . import serializers
from . import services, backends


class RegisterAPIView(views.APIView):
    
    def post(self, request: Request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            serializer.instance = services.create_user(user_dc=data)
            return response.Response(data=serializer.data)
        return response.Response(serializer.error_messages)