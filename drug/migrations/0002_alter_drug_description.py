# Generated by Django 3.2.5 on 2022-05-21 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]