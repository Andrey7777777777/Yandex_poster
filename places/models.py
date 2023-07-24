from django.core.validators import MinValueValidator
from django.db import models
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField('название', max_length=200)
    short_description = models.TextField('краткое описание', blank=True)
    long_description = HTMLField('полное описание', blank=True)
    latitude = models.FloatField('широта')
    longitude = models.FloatField('долгота')

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Places,
                              on_delete=models.CASCADE,
                              verbose_name='Место',
                              related_name='images'
                              )
    number = models.PositiveIntegerField(verbose_name='номер',
                                         validators=[
                                             MinValueValidator(1)
                                         ])

    image = models.ImageField(verbose_name='изображение')

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображение'
        ordering = ['number', 'place']
        unique_together = ['id', 'place', 'image']

    def __str__(self):
        return f'{self.number} {self.place.title}'


