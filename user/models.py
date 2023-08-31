from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, fullname, username, email, password=None):
        user = self.model(fullname=fullname, username=username, email=email, password=password)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, fullname, username, email, password):
        user = self.create_user(fullname, username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=256, unique=True, null=False, blank=False, verbose_name='email')
    username = models.CharField(max_length=40, unique=True, null=False, blank=False, verbose_name='username')
    fullname = models.CharField(max_length=100, null=False, verbose_name='fullname')
    is_online = models.BooleanField(default=False, verbose_name='is_online')
    is_staff = models.BooleanField(default=False, verbose_name='is_staff')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created_time')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='modified_time')

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'fullname', 'password']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
