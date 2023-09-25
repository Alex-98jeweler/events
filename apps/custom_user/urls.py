from django.urls import path

from . import views


urlpatterns = [
    path('user/', views.RegisterAPIView.as_view(), name='register'),
    path('auth/login/', views.LoginAPIView.as_view(), name='login')
    
]
