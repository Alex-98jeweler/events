from django.urls import path

from . import views


urlpatterns = [
    path('event/', views.ListCreateEventAPIView.as_view(), name='list-create-event'),
    path('event/<int:pk>/', views.UpdateEventAPIView.as_view(), name='update-event'),
    path('event/<int:pk>/', views.DestroyEventAPIView.as_view(), name='destroy-event'),
    path('event/<int:pk>/followers/', views.get_followers, ),
    path('event/<int:pk>/follow/', views.follow_event, name='follow-event'),
    path('event/<int:pk>/unfollow/', views.unfollow_event, name='unfollow-event')
]
