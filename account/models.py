from django.db import models
from django.contrib.auth.models import UserManager,AbstractUser
# Create your models here.


typeofusers = [('inspector','inspector'),('vendor','vendor'),('merchant','merchant')]

class User(AbstractUser):
    user_type = models.CharField(choices=typeofusers,max_length=10)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()



class UserRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    granted_on = models.DateTimeField()
    permission = models.NullBooleanField(default=None,null=True)
