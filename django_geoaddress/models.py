#--coding: utf8--

import requests

from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry


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
    country = models.ForeignKey(
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
    apartment = models.CharField(
        u'офис', max_length=10, blank=True)
    zip = models.CharField(
        u'почтовый индекс', max_length=10, blank=True)
    coordinates = models.PointField(
        u'координаты', blank=True, null=True)  # широта долгота

    # Используем GeoManager, чтобы делать ГЕО запросы
    objects = models.GeoManager()

    class Meta:
        verbose_name = u'адрес'
        verbose_name_plural = u'адреса'

    def __unicode__(self):
        return ', '.join(part for part in [self.zip, self.country.title,
                                           self.area, self.subarea,
                                           self.locality, self.street,
                                           self.house] if part)

    def fetch_coordinates(self):
        """
        Запрос координатов объекта с Яндекса.
        """
        query = ',+'.join(
            part for part in [self.country.title, self.area, self.subarea,
                              self.locality, self.street, self.house] if part)
        url = u'http://geocode-maps.yandex.ru/1.x/?geocode=%s&format=json' % (
            query)

        try:
            r = requests.get(url).json()
        except requests.exceptions.RequestException:
            return None

        try:
            latitude, longitude = (r['response']['GeoObjectCollection']
                                   ['featureMember'][0]['GeoObject']['Point']
                                   ['pos']).split(' ')
            return GEOSGeometry(U'POINT(%s %s)' % (latitude, longitude))
        except (KeyError, IndexError):
            return None

    def get_short_address(self):
        return ', '.join(part for part in [self.area, self.locality] if part)


class Region(models.Model):
    """
    Класс для географического региона.
    """
    name = models.CharField(u'название', max_length=255)
    coordinates = models.PolygonField(u'координаты')

    # Используем GeoManager, чтобы делать ГЕО запросы
    objects = models.GeoManager()

    class Meta:
        verbose_name = u'регион'
        verbose_name_plural = u'регионы'

    def __unicode__(self):
        return self.name
