# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Coordinate.convert'
        db.add_column(u'cyox_api_coordinate', 'convert',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Coordinate.convert'
        db.delete_column(u'cyox_api_coordinate', 'convert')


    models = {
        u'cyox_api.coordinate': {
            'Meta': {'ordering': "['request_made']", 'object_name': 'Coordinate'},
            'convert': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_point': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_made': ('django.db.models.fields.TimeField', [], {}),
            'start_point': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cyox_api']