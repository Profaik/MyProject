from django.db import models
from django.forms import forms
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_lenght=100)
    last_name=models.CharFeild(max_lenght=100)
    password=models.IntegerField(max_lenght=100)
    def get_participants(self):
        return EventUser.objects.filter(event=self)
class Sport_company(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    age = models.IntegerField(max_lenght=100)
    city = models.CharField(max_length=100)
    sport = models.IntegerField(max_length=100)
    userId = models.IntegerField(max_length=100)
    weight = models.FloatField(max_length= 100)