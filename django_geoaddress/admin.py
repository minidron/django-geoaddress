# --coding: utf8--
from django.contrib import admin
from django.contrib.gis import admin as gis_admin

from django_geoaddress.models import BaseAddress, Region
from django_geoaddress.forms import BaseAddressForm


@admin.register(BaseAddress)
class AddressAdmin(admin.ModelAdmin):
    form = BaseAddressForm
    list_display = ('__unicode__', 'coordinates', )


@admin.register(Region)
class RegionAdmin(gis_admin.OSMGeoAdmin):
    list_display = ('__unicode__', 'coordinates', )
    list_filter = ['name']
    search_fields = ['name']
    map_width = 900
    map_height = 500
