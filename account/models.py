from django.db import models
from django.contrib.auth.models import UserManager,AbstractUser
from django.contrib.postgres.fields import JSONField
# Create your models here.


typeofusers = [('inspector','inspector'),('vendor','vendor'),('merchant','merchant')]

class User(AbstractUser):
    user_type = models.CharField(choices=typeofusers,max_length=10)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()



class UserRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    granted_on = models.DateTimeField(null=True,blank=True)
    permission = models.NullBooleanField(default=None,null=True)

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name+" "+"as"+" "+self.user.username+" "+self.user.email+" "+"for role of"+" "+self.user.user_type


class Buyer(models.Model):
    buyer_name = models.CharField(max_length=25,null=False,blank=False)

    def __str__(self):
        return self.buyer_name


class Costsheet(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    madeon = models.DateTimeField(null=True,blank=True)
    sheet = JSONField()
