# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BudgetUser.program'
        db.add_column(u'budget_budgetuser', 'program',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)

        # Adding field 'BudgetUser.program_length'
        db.add_column(u'budget_budgetuser', 'program_length',
                      self.gf('django.db.models.fields.IntegerField')(default=5),
                      keep_default=False)

        # Adding field 'BudgetUser.current_year'
        db.add_column(u'budget_budgetuser', 'current_year',
                      self.gf('django.db.models.fields.IntegerField')(default=5),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BudgetUser.program'
        db.delete_column(u'budget_budgetuser', 'program')

        # Deleting field 'BudgetUser.program_length'
        db.delete_column(u'budget_budgetuser', 'program_length')

        # Deleting field 'BudgetUser.current_year'
        db.delete_column(u'budget_budgetuser', 'current_year')


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