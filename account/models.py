from django.db import models
from django.contrib.auth.models import User,UserManager,AbstractUser
# Create your models here.


typeofusers = [('admin','admin'),('inspector','inspector'),('vendor','vendor'),('merchant','merchant')]

class User(AbstractUser):
    user_type = models.CharField(choices=typeofusers,max_length=10)
    objects = UserManager()
