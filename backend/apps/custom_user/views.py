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


class LoginAPIView(views.APIView):
    
    def post(self, request: Request):
        username = request.data['username']
        password = request.data['password']
        
        user = services.user_username_selector(username)
        
        if user is None:
            raise exceptions.AuthenticationFailed("Invalid credentials")
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Invalid credentials")
        
        token = services.create_token(user_id=user.id)
        
        resp = response.Response()
        resp.data = {"access_token": token}
        
        return resp
    
class UsersMeAPiView(views.APIView):
    authentication_classes = [backends.JWTHeaderAuthentication, ]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request: Request):
        user = request.user
        serializer = serializers.UserSerializer(user)
        return response.Response(data=serializer.data)


class LogoutAPIView(views.APIView):
    authentication_classes = (backends.JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "so long farewell"}
        return resp
