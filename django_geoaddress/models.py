#--coding: utf8--

from django.contrib.gis.db import models


class Country(models.Model):
    """
    Модель страны.
    """
    title = models.CharField(
        u'название', max_length=255)

    class Meta:
        verbose_name = u'страна'
        verbose_name_plural = u'страны'
        ordering = ['title']

    def __unicode__(self):
        return self.title


class BaseAddress(models.Model):
    """
    Базовый класс адреса с ГЕО данными.
    """
    country = models.OneToOneField(
        Country,
        verbose_name=u'страна')
    area = models.CharField(
        u'область', max_length=255, blank=True)
    subarea = models.CharField(
        u'район', max_length=255, blank=True)
    locality = models.CharField(
        u'населенный пункт', max_length=255)
    street = models.CharField(
        u'улица', max_length=255, blank=True)
    house = models.CharField(
        u'дом', max_length=50, blank=True)
    zip = models.CharField(
        u'почтовый индекс', max_length=10, blank=True)
    coordinates = models.PointField(
        u'координаты', blank=True, null=True)  # широта долгота

    # Используем GeoManager, чтобы делать ГЕО запросы
    manager = models.GeoManager()

    class Meta:
        verbose_name = u'адрес'
        verbose_name_plural = u'адреса'
