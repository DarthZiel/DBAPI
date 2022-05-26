from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fio = models.CharField(max_length=100)
    REQUIRED_FIELDS = ["fio"]
CATEGORY = [
    ('Без категории', 'Без категории'), ('Вторая категория', 'Вторая категория'), ('Первая категория', 'Первая категория'), ('Высшая категория','Высшая категория')
]
SEX = [('мужчина', 'мужчина'), ('женщина','женщина')]
class Profile(models.Model):

    fio = models.CharField(max_length=100)
    position = models.ForeignKey("Position", on_delete=models.CASCADE,blank=True)
    date_of_birth = models.DateField(verbose_name='дата рождения')
    structure = models.ForeignKey('Structure', on_delete=models.CASCADE,blank=True)
    schedule = models.CharField(max_length=100, verbose_name='Часы приема')
    cabinet = models.CharField(max_length=15, verbose_name='Кабинет')
    photo = models.ImageField(blank=True)

    experience = models.CharField(max_length=100, verbose_name='стаж')
    sex = models.CharField(max_length=100,choices=SEX, verbose_name='пол')
    Category = models.CharField(max_length=100, choices=CATEGORY, default=CATEGORY[0])
    diploma = models.FileField(blank=True)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
class Structure(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Структура"
        verbose_name_plural = "Структуры"
