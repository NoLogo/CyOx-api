# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Coordinate'
        db.create_table(u'cyox_api_coordinate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_point', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('end_point', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('request_made', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'cyox_api', ['Coordinate'])


    def backwards(self, orm):
        # Deleting model 'Coordinate'
        db.delete_table(u'cyox_api_coordinate')


    models = {
        u'cyox_api.coordinate': {
            'Meta': {'ordering': "['request_made']", 'object_name': 'Coordinate'},
            'end_point': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_made': ('django.db.models.fields.TimeField', [], {}),
            'start_point': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cyox_api']