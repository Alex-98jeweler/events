from django import forms
from django.core.exceptions import ValidationError

from .models import User


   
class UserCreationForm(forms.ModelForm):
    birthday = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label="Дата Рождения"
    )
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput({'class': 'form-control'}), label="Повторите пароль")
    field_order = ['username', 'password', 'password2', 'first_name', 'last_name', 'birthday']
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'birthday')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput({'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def clean_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password1
        
    
    