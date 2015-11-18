# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'django_geoaddress_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'django_geoaddress', ['Country'])

        # Adding model 'BaseAddress'
        db.create_table(u'django_geoaddress_baseaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_geoaddress.Country'])),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('subarea', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('locality', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('house', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('coordinates', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'django_geoaddress', ['BaseAddress'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'django_geoaddress_country')

        # Deleting model 'BaseAddress'
        db.delete_table(u'django_geoaddress_baseaddress')


    models = {
        u'django_geoaddress.baseaddress': {
            'Meta': {'object_name': 'BaseAddress'},
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