from django.test import TestCase
from core.models import User, Sport_company # Переименовать модель Sport_company и изменить импорт
from django.contrib.auth.models import User
# Create your tests here.

# ДАННЫЙ ТЕСТ ПЛАГИАТ !!! Вы будете наказаны, штраф 500 социальных кредитов
class UserTest(TestCase):
    def test_event_model_create(self):
        user = User.objects.create(username="Test") # Создадим пользователя
        # он будет автором события
        participant1 = User.objects.create(username="Участник события №1")
        participant2 = User.objects.create(username="Участник события №2")
        newEvent = User.objects.create(
            name="Тестовое событие",
            game=1,
            date="2021-12-13 16:20",
            author=user,
            description="Test",
            status=1,
            recording="https://test.com"
        ) # это newUser, никак не newEvent, да и параметры напоминаюь модель Event из чужого проекта! ПЛАГИАТ! ШТРАФ 500 СОЦИАЛЬНЫХ КРЕДИТОВ
        self.assertEqual(newEvent.name, "Тестовое событие")
        eventUser1 = Sport_company.objects.create(event=newEvent, user=participant1) # eventUser - неуместное название переменной (мождет быть company1 ?)!!!
        eventUser2 = Sport_company.objects.create(event=newEvent, user=participant2) # company2?
        self.assertEqual(newEvent.get_participants()[0].user, participant1) # проверяем что участник 1 является участником события
        self.assertEqual(newEvent.get_participants()[1].user, participant2) # проверяем что участник 2 является участником события
# Create your tests here.
