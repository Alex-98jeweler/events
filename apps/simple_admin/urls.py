from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('dashboard/', views.DashboardView.as_view()),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.RegistrationView.as_view()),
    path('events/', views.EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventDetalView.as_view(), name='event-detail')
    
]