#--coding: utf8--

from django import forms


class AddressWidget(forms.TextInput):

    class Media:
        css = {
            'all': ('django_geoaddress/css/jquery.geoaddress.css',)
        }
        js = (
            'django_geoaddress/js/jquery.autocomplete.min.js',
            'django_geoaddress/js/jquery.geoaddress.js',
        )

    def __init__(self, attrs=None):
        final_attrs = {
            'class': 'geoaddress',
        }
        if attrs is not None:
            final_attrs.update(attrs)
        super(AddressWidget, self).__init__(final_attrs)
