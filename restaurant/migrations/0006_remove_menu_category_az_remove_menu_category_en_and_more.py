# Generated by Django 4.0.5 on 2022-06-23 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_category_name_az_category_name_en_category_name_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='category_az',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='category_en',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='category_ru',
        ),
    ]
