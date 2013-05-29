# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BudgetData'
        db.delete_table(u'budget_budgetdata')

        # Adding model 'BudgetPlanningData'
        db.create_table(u'budget_budgetplanningdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('modified', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'budget', ['BudgetPlanningData'])


    def backwards(self, orm):
        # Adding model 'BudgetData'
        db.create_table(u'budget_budgetdata', (
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'budget', ['BudgetData'])

        # Deleting model 'BudgetPlanningData'
        db.delete_table(u'budget_budgetplanningdata')


    models = {
        u'budget.budgetplanningdata': {
            'Meta': {'object_name': 'BudgetPlanningData'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '10'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'budget.budgetuser': {
            'Meta': {'object_name': 'BudgetUser'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'sequence': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['budget']