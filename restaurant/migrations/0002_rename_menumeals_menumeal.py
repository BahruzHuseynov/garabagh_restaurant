# Generated by Django 4.0.5 on 2022-06-22 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuMeals',
            new_name='MenuMeal',
        ),
    ]