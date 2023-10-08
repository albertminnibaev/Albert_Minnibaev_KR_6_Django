from django.contrib.auth.models import AbstractUser
from django.db import models

from service.models import NULLABLE


# Create your models here.

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    verification = models.CharField(max_length=20, **NULLABLE, verbose_name='верификация')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
