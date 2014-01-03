# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'oil_gas_project_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('info', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal(u'oil_gas_project', ['Project'])

        # Adding model 'ProjectAsset'
        db.create_table(u'oil_gas_project_projectasset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oil_gas_project.Project'])),
        ))
        db.send_create_signal(u'oil_gas_project', ['ProjectAsset'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'oil_gas_project_project')

        # Deleting model 'ProjectAsset'
        db.delete_table(u'oil_gas_project_projectasset')


    models = {
        u'oil_gas_project.activitymap': {
            'Meta': {'object_name': 'ActivityMap'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'oil_gas_project.contactinfo': {
            'Meta': {'object_name': 'ContactInfo'},
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'oil_gas_project.focusarea': {
            'Meta': {'object_name': 'FocusArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'oil_gas_project.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'oil_gas_project.projectasset': {
            'Meta': {'object_name': 'ProjectAsset'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oil_gas_project.Project']"})
        }
    }

    complete_apps = ['oil_gas_project']