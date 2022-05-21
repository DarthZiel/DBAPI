from django.db import models

# Create your models here.
class Drug(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    photo = models.ImageField()
    price = models.IntegerField()
    count = models.IntegerField()

