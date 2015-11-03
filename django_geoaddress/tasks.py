# --coding: utf8--
from celery import shared_task

from django_geoaddress.models import BaseAddress


@shared_task(name='django_geoaddress.tasks.set_coordinates')
def set_coordinates(instance):
    """
    Сохранить координаты для адреса.
    """
    (BaseAddress.objects
     .filter(pk=instance.pk)
     .update(coordinates=instance.fetch_coordinates()))
