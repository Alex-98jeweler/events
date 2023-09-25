from django.urls import path

from . import views


urlpatterns = [
    path('event/', views.ListCreateEventAPIView.as_view(), name='list-create-event'),
    path('event/<int:pk>/', views.UpdateEventAPIView.as_view(), name='update-event'),
    path('event/<int:pk>/', views.DestroyEventAPIView.as_view(), name='destroy-event')
]
