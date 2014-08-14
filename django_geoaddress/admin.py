# coding=utf-8

from django.contrib import admin

from django_geoaddress.models import BaseAddress, Region
from django_geoaddress.forms import BaseAddressForm, RegionForm


class AddressAdmin(admin.ModelAdmin):
    form = BaseAddressForm
    list_display = ('__unicode__', 'coordinates', )

admin.site.register(BaseAddress, AddressAdmin)


class RegionAdmin(admin.ModelAdmin):
    form = RegionForm
    list_display = ('__unicode__', 'coordinates', )

admin.site.register(Region, RegionAdmin)
