# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Category', fields ['code']
        db.create_unique(u'stocks_category', ['code'])

        # Adding unique constraint on 'Category', fields ['description']
        db.create_unique(u'stocks_category', ['description'])


    def backwards(self, orm):
        # Removing unique constraint on 'Category', fields ['description']
        db.delete_unique(u'stocks_category', ['description'])

        # Removing unique constraint on 'Category', fields ['code']
        db.delete_unique(u'stocks_category', ['code'])


    models = {
        u'stocks.category': {
            'Meta': {'object_name': 'Category'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '6'}),
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['stocks']