from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView



class DashboardView(View):
    pass


class LoginView(LoginView):
    
    template_name = "simple_admin/login.html"
    
    def get_success_url(self) -> str:
        return super().get_success_url()
    


class RegistrationView(View):
    pass



