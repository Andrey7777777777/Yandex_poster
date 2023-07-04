from django.db import models


# Create your models here.
class Places(models.Model):
    title = models.CharField('название', max_length=200)
    short_description = models.TextField('краткое описание ')
    long_description = models.TextField('полное описание')
    latitude = models.FloatField('широта')
    longitude = models.FloatField('долгота')

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
    image_number = models.IntegerField()

    image = models.ImageField()

    def __str__(self):
        return f'{self.image_number} {self.place.title}'

    class Meta:
        verbose_name = 'IMAGE'
        verbose_name_plural = 'IMAGES'