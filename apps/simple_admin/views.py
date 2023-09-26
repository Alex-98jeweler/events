from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin



class DashboardView(LoginRequiredMixin, View):
    login_url = "/login/"
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name='simple_admin/dashboard.html')


class LoginView(LoginView):
    
    template_name = "simple_admin/login.html"
    
    def get_redirect_url(self) -> str:
        return "/dashboard/"
    
    
    
def logout_view(request):
    logout(request)
    return redirect("/login/")
    

class RegistrationView(View):
    pass



