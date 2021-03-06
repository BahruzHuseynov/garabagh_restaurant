# Generated by Django 4.0.5 on 2022-06-23 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_remove_menumeal_price_az_remove_menumeal_price_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='picture',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='restaurant.category'),
        ),
        migrations.AlterField(
            model_name='menumeal',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_meals', to='restaurant.menu'),
        ),
    ]
