from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self,
        first_name: str,
        last_name: str,
        username: str,
        password: str = None,
        is_staff=False,
        is_superuser=False,
    ) -> "User":
        if not username:
            raise ValueError("User must have an username")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(username=username)
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(
        self, first_name: str, last_name: str, username: str, password: str
    ) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        return user


class User(AbstractUser):
    
    username = models.CharField("Логин", max_length=32, unique=True)
    first_name = models.CharField("Имя", max_length=32)
    last_name = models.CharField("Фамилия", max_length=32)
    password = models.CharField("Пароль", max_length=255)
    birthday = models.DateField("Дата Рождения", null=True)
    email=None
    
    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'username'
    
    objects = UserManager()
    
