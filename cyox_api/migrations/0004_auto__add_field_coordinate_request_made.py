# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Coordinate.request_made'
        db.add_column(u'cyox_api_coordinate', 'request_made',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Coordinate.request_made'
        db.delete_column(u'cyox_api_coordinate', 'request_made')


    models = {
        u'cyox_api.coordinate': {
            'Meta': {'ordering': "['request_made']", 'object_name': 'Coordinate'},
            'end_point': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_made': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'start_point': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cyox_api']