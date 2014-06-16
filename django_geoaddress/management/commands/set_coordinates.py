# coding=utf-8

from django.core.management.base import NoArgsCommand
from django.contrib.gis.geos import GEOSGeometry

from django_geoaddress.models import BaseAddress


class Command(NoArgsCommand):
    """
    Поиск адресов без координат и попытка их проставить.
    """
    def handle_noargs(self, **options):
        addresses = BaseAddress.objects.filter(coordinates__isnull=True)
        for address in addresses:
            try:
                address.coordinates = GEOSGeometry(address.fetch_coordinates())
                self.stdout.write(u'[%s, %s] - %s' % (address.coordinates.x,
                                                      address.coordinates.y,
                                                      address))
                address.save()
            except TypeError:
                self.stdout.write(u'pk %s - не удалось получить координаты' %
                                  (address.pk))
