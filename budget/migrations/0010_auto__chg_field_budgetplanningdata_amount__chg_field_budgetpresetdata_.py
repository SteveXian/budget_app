# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BudgetPlanningData.amount'
        db.alter_column(u'budget_budgetplanningdata', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2))

        # Changing field 'BudgetPresetData.amount'
        db.alter_column(u'budget_budgetpresetdata', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'BudgetPlanningData.amount'
        db.alter_column(u'budget_budgetplanningdata', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10))

        # Changing field 'BudgetPresetData.amount'
        db.alter_column(u'budget_budgetpresetdata', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10))

    models = {
        u'budget.budgetplanningdata': {
            'Meta': {'object_name': 'BudgetPlanningData'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'budget.budgetpresetdata': {
            'Meta': {'object_name': 'BudgetPresetData'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'coop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'budget.budgetuser': {
            'Meta': {'object_name': 'BudgetUser'},
            'coop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'current_year': ('django.db.models.fields.IntegerField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'program_length': ('django.db.models.fields.IntegerField', [], {}),
            'sequence': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['budget']