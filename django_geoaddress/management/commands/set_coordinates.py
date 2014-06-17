# coding=utf-8

from django.core.management.base import NoArgsCommand

from django_geoaddress.models import BaseAddress


class Command(NoArgsCommand):
    """
    Поиск адресов без координат и попытка их проставить.
    """
    def handle_noargs(self, **options):
        addresses = BaseAddress.objects.filter(coordinates__isnull=True)
        for address in addresses:
            if address.fetch_coordinates():
                address.coordinates = address.fetch_coordinates()
                self.stdout.write(u'[%s, %s] - %s' % (address.coordinates.x,
                                                      address.coordinates.y,
                                                      address))
                address.save()
            else:
                self.stdout.write(u'pk %s - не удалось получить координаты' %
                                  (address.pk))
