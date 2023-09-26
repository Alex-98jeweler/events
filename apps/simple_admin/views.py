from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from ..custom_user.models import User
from ..custom_user.forms import UserCreationForm



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
    

    
   
