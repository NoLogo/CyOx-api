# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Coordinate.convert'
        db.delete_column(u'cyox_api_coordinate', 'convert')

        # Deleting field 'Coordinate.request_made'
        db.delete_column(u'cyox_api_coordinate', 'request_made')


    def backwards(self, orm):
        # Adding field 'Coordinate.convert'
        db.add_column(u'cyox_api_coordinate', 'convert',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Coordinate.request_made'
        db.add_column(u'cyox_api_coordinate', 'request_made',
                      self.gf('django.db.models.fields.TimeField')(default=0),
                      keep_default=False)


    models = {
        u'cyox_api.coordinate': {
            'Meta': {'object_name': 'Coordinate'},
            'end_point': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_point': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cyox_api']