from typing import Any
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
    field_order = ['first_name', 'last_name', 'birthday', 'username', 'password', 'password2',]
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
        password1 = self.data.get('password')
        password2 = self.data.get('password2')
        if password1 != password2:
            print(password1, password2)
            raise ValidationError("Пароли не совпадают")
        return password1
    
    def save(self, commit: bool = ...) -> Any:
        self.cleaned_data.pop('password2')
        user = User(**self.cleaned_data)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user

    
    