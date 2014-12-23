# coding=utf-8

from django.contrib import admin
from django.contrib.gis import admin as gis_admin

from django_geoaddress.models import BaseAddress, Region
from django_geoaddress.forms import BaseAddressForm


class AddressAdmin(admin.ModelAdmin):
    form = BaseAddressForm
    list_display = ('__unicode__', 'coordinates', )

admin.site.register(BaseAddress, AddressAdmin)


class RegionAdmin(gis_admin.OSMGeoAdmin):
    list_display = ('__unicode__', 'coordinates', )
    map_width = 900
    map_height = 500

admin.site.register(Region, RegionAdmin)
