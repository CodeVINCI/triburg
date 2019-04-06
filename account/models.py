from django.db import models
from django.contrib.auth.models import User,UserManager,AbstractUser
# Create your models here.




class User(AbstractUser):
    user_type = models.CharField()
    objects = UserManager()
