from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from ..custom_user.models import User
from ..custom_user.forms import UserCreationForm
from ..events.models import Event, EventFollower

def index(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return redirect('/dashboard/')
        

class DashboardView(LoginRequiredMixin, View):
    login_url = "/login/"
    
    def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, template_name='simple_admin/index.html', context={'user': user})


class LoginView(LoginView):
    
    template_name = "simple_admin/login.html"
    
    def get_redirect_url(self) -> str:
        return "/dashboard/"
    
    
    
def logout_view(request):
    logout(request)
    return redirect("/login/")
    

class RegistrationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'simple_admin/registration.html'
    success_url = '/login/'

class EventListView(ListView, LoginRequiredMixin):
    template_name = 'simple_admin/events-list.html'
    model = Event
    
    def get_context_data(self, **kwargs: Any):
        events = self.model.objects.all()
        return {"events": events}
    

class MyEventsList(ListView, LoginRequiredMixin):
    template_name = 'simple_admin/my-events.html'
    model = Event
    
    def get_context_data(self, **kwargs: Any):
        user = self.request.user
        follower_events = EventFollower.objects.filter(follower=user)
        events = [follower_event.event for follower_event in follower_events]
        return {'events': events}
        
    
class EventDetalView(DetailView, LoginRequiredMixin):
    
    template_name='simple_admin/events-detail.html'
    model = Event
    
    def get_context_data(self, **kwargs: Any):
        event = self.get_object()
        user = self.request.user
        eventfollowers = EventFollower.objects.filter(event=event)
        followers = [eventfollower.follower for eventfollower in eventfollowers]
        return {'event': event, 'followers': followers, 'curr_user': user}


def event_follow(request, *args, **kwargs):
    pk = kwargs.get('pk')
    user = request.user
    event = Event.objects.get(pk=pk)
    try:
        EventFollower.objects.create(event=event, follower=user)
    except:
        pass
    return redirect(f'/events/{pk}/')

def event_unfollow(request, *args, **kwargs):
    event_id = kwargs.get('pk')
    user = request.user
    event = Event.objects.get(pk=event_id)
    event_follower = EventFollower.objects.get(event=event, follower=user)
    try:
        event_follower.delete()
    except:
        pass
    return redirect(f'/events/{event_id}/')
    


class FollowerDetailView(DetailView, LoginRequiredMixin):
    template_name = 'simple_admin/follower-detail.html'
    model = User
    
    def get_context_data(self, **kwargs: Any):
        back_event_pk = self.request.GET.get("back_to_event")
        user = self.get_object()
        return {'user': user, 'event_pk': back_event_pk}