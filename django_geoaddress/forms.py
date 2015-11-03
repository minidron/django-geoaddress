# --coding: utf8--
from django.contrib.gis import forms
from django.conf import settings

from django_geoaddress.models import BaseAddress, Country
from django_geoaddress.widgets import AddressWidget

DEFAULT_COUNTRY = getattr(settings, 'DEFAULT_COUNTRY', 0)


class BaseAddressForm(forms.ModelForm):
    suggestion = forms.CharField(
        label=u'Быстрый поиск адреса', required=False, widget=AddressWidget,
        help_text=u'Поиск адреса. Вводить через запятую. Например: Россия, '
                  u'Серпухов, Советская, 69/22')

    class Meta:
        model = BaseAddress
        fields = ['suggestion', 'country', 'area', 'subarea', 'locality',
                  'street', 'house', 'apartment', 'zip', 'coordinates']
        widgets = {
            'country': forms.Select(
                attrs={'data-address-type': 'country'}),
            'area': forms.TextInput(
                attrs={'data-address-type': 'area'}),
            'subarea': forms.TextInput(
                attrs={'data-address-type': 'subarea'}),
            'locality': forms.TextInput(
                attrs={'data-address-type': 'locality'}),
            'street': forms.TextInput(
                attrs={'data-address-type': 'street'}),
            'house': forms.TextInput(
                attrs={'data-address-type': 'house'}),
            'coordinates': forms.OSMWidget,
        }

    def __init__(self, *args, **kwargs):
        super(BaseAddressForm, self).__init__(*args, **kwargs)
        self.fields['country'].initial = DEFAULT_COUNTRY
        if self.instance.pk:
            COUNTRY = u'%s, ' % self.instance.country
        elif DEFAULT_COUNTRY == 0:
            COUNTRY = u''
        else:
            COUNTRY = u'%s, ' % Country.objects.get(pk=DEFAULT_COUNTRY)
        self.fields['suggestion'].initial = COUNTRY

    def save(self, commit=True):
        instance = super(BaseAddressForm, self).save(commit=False)
        if not set(['area', 'subarea', 'locality', 'street', 'house',
                    'apartment', 'zip']).isdisjoint(self.changed_data):
            if 'coordinates' not in self.changed_data:
                instance.coordinates = instance.fetch_coordinates()
        return instance
