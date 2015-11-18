# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BaseAddress.apartment'
        db.add_column(u'django_geoaddress_baseaddress', 'apartment',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BaseAddress.apartment'
        db.delete_column(u'django_geoaddress_baseaddress', 'apartment')


    models = {
        u'django_geoaddress.baseaddress': {
            'Meta': {'object_name': 'BaseAddress'},
            'apartment': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'coordinates': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_geoaddress.Country']"}),
            'house': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subarea': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'django_geoaddress.country': {
            'Meta': {'ordering': "['title']", 'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['django_geoaddress']