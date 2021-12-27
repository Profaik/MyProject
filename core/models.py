from django.db import models
from django.forms import forms
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model): # Не создавайте модель своего пользователя, если используете базовую Django, иначе наследуйтесь от AbstractBaseUser вместо models.Model
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100) # Опечатка в слове max_length
    password=models.IntegerField(max_length=100) # Опечатка в слове max_length
    def get_participants(self):
        return EventUser.objects.filter(event=self) # Модель EventUser явно не из вашего проекта

class Sport_company(models.Model): # В нотации PEP8 питона, названия классаов формируются как SportCompany, а вот переменных, sport_company
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    age = models.IntegerField(max_length=100)  # Опечатка в слове max_length
    city = models.CharField(max_length=100)
    sport = models.IntegerField(max_length=100)
    userId = models.IntegerField(max_length=100)
    weight = models.FloatField(max_length= 100)