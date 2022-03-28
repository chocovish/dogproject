from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

class User(AbstractUser):
    collar_colour = models.CharField(max_length=10,default="red")
    nickname =  models.CharField(max_length=20,default="morty")
    course = models.CharField(max_length=30,null=False,blank=False)
    email = models.EmailField(max_length=50,unique=True,null=False,blank=False)
    username = models.CharField(max_length=50,null=True,blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname","username"]

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30,null=False,blank=False)
    desc = models.CharField(max_length=50,null=True,blank=True)
    event_date = models.DateTimeField(null=False,blank=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username+"|"+self.title

class Reward(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.DO_NOTHING,null=True)
    point = models.PositiveSmallIntegerField(null=False,blank=False,default=10)
    date = models.DateTimeField(auto_now_add=True)

