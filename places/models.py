from django.core.validators import MinValueValidator
from django.db import models
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField('название', default='default title', max_length=200)
    short_description = models.TextField('краткое описание', blank=True)
    long_description = HTMLField('полное описание', blank=True)
    latitude = models.FloatField('широта')
    longitude = models.FloatField('долгота')
    place_id = models.CharField('ID места',
                                max_length=200,
                                unique=True,
                                blank=True,
                                null=True
                                )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'PLACE'
        verbose_name_plural = 'PLACES'


class Image(models.Model):
    place = models.ForeignKey(Places,
                              on_delete=models.CASCADE,
                              verbose_name='Место',
                              related_name='images'
                              )
    image_number = models.PositiveIntegerField(validators=[
        MinValueValidator(1)
    ])

    image = models.ImageField()

    def __str__(self):
        return f'{self.image_number} {self.place.title}'

    class Meta:
        verbose_name = 'IMAGE'
        verbose_name_plural = 'IMAGES'
        ordering = ['image_number', 'place']
