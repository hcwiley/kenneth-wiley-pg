# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactInfo'
        db.create_table(u'oil_gas_project_contactinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('info', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
        ))
        db.send_create_signal(u'oil_gas_project', ['ContactInfo'])


    def backwards(self, orm):
        # Deleting model 'ContactInfo'
        db.delete_table(u'oil_gas_project_contactinfo')


    models = {
        u'oil_gas_project.contactinfo': {
            'Meta': {'object_name': 'ContactInfo'},
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['oil_gas_project']