from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None
    name = models.CharField(max_length=110, )
    username = models.CharField(max_length=110, unique=True)
    password = models.CharField(max_length=110)
    profile_picture = models.ImageField(upload_to='profile-pictures/', default='profile-pictures/default.png')

    USERNAME_FIELD = 'username'
