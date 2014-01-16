# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ContactInfo.phone2'
        db.delete_column(u'oil_gas_project_contactinfo', 'phone2')

        # Deleting field 'ContactInfo.phone'
        db.delete_column(u'oil_gas_project_contactinfo', 'phone')

        # Adding field 'ContactInfo.cell'
        db.add_column(u'oil_gas_project_contactinfo', 'cell',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'ContactInfo.office'
        db.add_column(u'oil_gas_project_contactinfo', 'office',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ContactInfo.phone2'
        db.add_column(u'oil_gas_project_contactinfo', 'phone2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ContactInfo.phone'
        db.add_column(u'oil_gas_project_contactinfo', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'ContactInfo.cell'
        db.delete_column(u'oil_gas_project_contactinfo', 'cell')

        # Deleting field 'ContactInfo.office'
        db.delete_column(u'oil_gas_project_contactinfo', 'office')


    models = {
        u'oil_gas_project.activitymap': {
            'Meta': {'object_name': 'ActivityMap'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'oil_gas_project.contactinfo': {
            'Meta': {'object_name': 'ContactInfo'},
            'cell': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'office': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'})
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
            'full_res_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oil_gas_project.Project']"})
        }
    }

    complete_apps = ['oil_gas_project']