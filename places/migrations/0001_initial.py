# Generated by Django 4.0 on 2023-07-10 14:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('short_description', models.TextField(blank=True, verbose_name='краткое описание')),
                ('long_description', models.TextField(blank=True, verbose_name='полное описание')),
                ('latitude', models.FloatField(null=True, verbose_name='широта')),
                ('longitude', models.FloatField(null=True, verbose_name='долгота')),
                ('place_id', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='ID места')),
            ],
            options={
                'verbose_name': 'PLACE',
                'verbose_name_plural': 'PLACES',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('image', models.ImageField(upload_to='')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.places', verbose_name='Место')),
            ],
            options={
                'verbose_name': 'IMAGE',
                'verbose_name_plural': 'IMAGES',
            },
        ),
    ]
