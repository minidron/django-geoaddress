# coding=utf-8

from django.core.management.base import NoArgsCommand

from django_geoaddress.models import BaseAddress


class Command(NoArgsCommand):
    """
    Поиск адресов без координат и попытка их проставить.
    """
    def handle_noargs(self, **options):
        for address in BaseAddress.objects.all():
            (BaseAddress.objects.filter(pk=address.pk)
                .update(coordinates=address.fetch_coordinates()))
