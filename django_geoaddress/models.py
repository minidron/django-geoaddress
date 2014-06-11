#--coding: utf8--

from collections import OrderedDict

from django.contrib.gis.db import models

from django_geoaddress import geocooders


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
    objects = models.GeoManager()

    class Meta:
        verbose_name = u'адрес'
        verbose_name_plural = u'адреса'

    def fetch_coordinates(self):
        """
        Получить координаты.
        """
        data = OrderedDict([
            ('country', self.country.title),
            ('area', self.area),
            ('subarea', self.subarea),
            ('locality', self.locality),
            ('street', self.street),
            ('house', self.house),
        ])
        return geocooders.yandex(data)
