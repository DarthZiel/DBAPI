from django.db import models

# Create your models here.
class Drug(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название лекарства')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(verbose_name='фото лекарства')
    price = models.IntegerField(verbose_name='цена')
    count = models.IntegerField(verbose_name='количество на складе')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Лекарство'
        verbose_name_plural = 'Лекарства'