# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stock'
        db.create_table(u'stocks_stock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('barcode', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('uom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['uom.UOM'])),
            ('discontinued', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'stocks', ['Stock'])


    def backwards(self, orm):
        # Deleting model 'Stock'
        db.delete_table(u'stocks_stock')


    models = {
        u'stocks.category': {
            'Meta': {'object_name': 'Category'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '6'}),
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'barcode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stocks.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'discontinued': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['uom.UOM']"})
        },
        u'uom.uom': {
            'Meta': {'object_name': 'UOM'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['stocks']