# Generated by Django 3.2.5 on 2022-05-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220526_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Type_of_education',
        ),
        migrations.AddField(
            model_name='profile',
            name='Category',
            field=models.CharField(choices=[('Без категории', 'Без категории'), ('Вторая категория', 'Вторая категория'), ('Первая категория', 'Первая категория'), ('Высшая категория', 'Высшая категория')], default=('Без категории', 'Без категории'), max_length=100),
        ),
    ]
