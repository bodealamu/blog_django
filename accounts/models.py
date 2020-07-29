from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    pass


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model in django using the Abstract base user class
    """
    first_name = models.CharField(max_length=30, verbose_name='First name')
    last_name = models.CharField(max_length=30, verbose_name='Last name')
    email = models.EmailField(max_length=100, verbose_name='Email Address', unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        firstname = self.first_name
        lastname = self.last_name

        fullname = str(firstname) + ' ' + str(lastname)
        return fullname

