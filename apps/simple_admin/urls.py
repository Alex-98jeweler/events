from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('dashboard/', views.DashboardView.as_view()),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.RegistrationView.as_view()),
    path('events/', views.EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventDetalView.as_view(), name='event-detail'),
    path('events/<int:pk>/follow/', views.event_follow, name='event-detail'),
    path('events/<int:pk>/unfollow/', views.event_unfollow, name='event-detail'),
    path('followers/<int:pk>/', views.FollowerDetailView.as_view(), name='follower-detail'),
    path('my-events/', views.MyEventsList.as_view(), name='my-events-list'),
    
]