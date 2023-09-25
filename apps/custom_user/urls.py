from django.urls import path

from . import views


urlpatterns = [
    path('user/', views.RegisterAPIView.as_view(), name='register'),
    path('user/me/', views.UsersMeAPiView.as_view(), name='me'),
    path('auth/login/', views.LoginAPIView.as_view(), name='login'),
    path('auth/logout/', views.LogoutAPIView.as_view(), name='logout')
    
]
