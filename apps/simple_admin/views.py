from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from ..custom_user.models import User
from ..custom_user.forms import UserCreationForm
from ..events.models import Event, EventFollower


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
    

class EventListView(ListView, LoginRequiredMixin):
    template_name = 'simple_admin/events-list.html'
    model = Event
    
    def get_context_data(self, **kwargs: Any):
        events = self.model.objects.all()
        return {"events": events}
    
class EventDetalView(DetailView, LoginRequiredMixin):
    
    template_name='simple_admin/events-detail.html'
    model = Event
    
    def get_context_data(self, **kwargs: Any):
        event = self.get_object()
        followers = EventFollower.objects.filter(event=event)
        followers = [follower.follower for follower in followers]
        return {'event': event, 'followers': followers}


def event_follow(request, *args, **kwargs):
    pk = kwargs.get('pk')
    user = request.user
    event = Event.objects.get(pk=pk)
    EventFollower.objects.create(event=event, follower=user)
    return redirect(f'/events/{pk}/')