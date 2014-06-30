# coding=utf-8

from django.contrib import admin

from django_geoaddress.models import BaseAddress
from django_geoaddress.forms import BaseAddressForm


class AddressAdmin(admin.ModelAdmin):
    form = BaseAddressForm
    list_display = ('__unicode__', 'coordinates', )


admin.site.register(BaseAddress, AddressAdmin)
