# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BudgetUser.last_name'
        db.delete_column(u'budget_budgetuser', 'last_name')

        # Deleting field 'BudgetUser.first_name'
        db.delete_column(u'budget_budgetuser', 'first_name')

        # Deleting field 'BudgetUser.program'
        db.delete_column(u'budget_budgetuser', 'program')

        # Adding field 'BudgetUser.start_year'
        db.add_column(u'budget_budgetuser', 'start_year',
                      self.gf('django.db.models.fields.IntegerField')(default=2008),
                      keep_default=False)

        # Adding field 'BudgetUser.end_year'
        db.add_column(u'budget_budgetuser', 'end_year',
                      self.gf('django.db.models.fields.IntegerField')(default=2013),
                      keep_default=False)

        # Adding field 'BudgetUser.saved'
        db.add_column(u'budget_budgetuser', 'saved',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=19, decimal_places=2),
                      keep_default=False)

        # Adding field 'BudgetUser.owned'
        db.add_column(u'budget_budgetuser', 'owned',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=19, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'BudgetUser.last_name'
        db.add_column(u'budget_budgetuser', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'BudgetUser.first_name'
        db.add_column(u'budget_budgetuser', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=100),
                      keep_default=False)

        # Adding field 'BudgetUser.program'
        db.add_column(u'budget_budgetuser', 'program',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=500),
                      keep_default=False)

        # Deleting field 'BudgetUser.start_year'
        db.delete_column(u'budget_budgetuser', 'start_year')

        # Deleting field 'BudgetUser.end_year'
        db.delete_column(u'budget_budgetuser', 'end_year')

        # Deleting field 'BudgetUser.saved'
        db.delete_column(u'budget_budgetuser', 'saved')

        # Deleting field 'BudgetUser.owned'
        db.delete_column(u'budget_budgetuser', 'owned')


    models = {
        u'budget.budgetplanningdata': {
            'Meta': {'object_name': 'BudgetPlanningData'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'income': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'budget.budgettrackingdata': {
            'Meta': {'object_name': 'BudgetTrackingData'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'budget.budgetuser': {
            'Meta': {'object_name': 'BudgetUser'},
            'coop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'current_term': ('django.db.models.fields.IntegerField', [], {}),
            'current_year': ('django.db.models.fields.IntegerField', [], {}),
            'end_year': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'owned': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'program_length': ('django.db.models.fields.IntegerField', [], {}),
            'saved': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'sequence': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_year': ('django.db.models.fields.IntegerField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['budget']