# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BudgetUser.start_year'
        db.alter_column(u'budget_budgetuser', 'start_year', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'BudgetUser.end_year'
        db.alter_column(u'budget_budgetuser', 'end_year', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'BudgetUser.owned'
        db.alter_column(u'budget_budgetuser', 'owned', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=19, decimal_places=2))

        # Changing field 'BudgetUser.tuition'
        db.alter_column(u'budget_budgetuser', 'tuition', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=19, decimal_places=2))

        # Changing field 'BudgetUser.program_length'
        db.alter_column(u'budget_budgetuser', 'program_length', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'BudgetUser.saved'
        db.alter_column(u'budget_budgetuser', 'saved', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=19, decimal_places=2))

        # Changing field 'BudgetUser.current_year'
        db.alter_column(u'budget_budgetuser', 'current_year', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'BudgetPlanningData.term'
        db.alter_column(u'budget_budgetplanningdata', 'term', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'BudgetPlanningData.year'
        db.alter_column(u'budget_budgetplanningdata', 'year', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'BudgetPlanningData.label'
        db.alter_column(u'budget_budgetplanningdata', 'label', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'BudgetPlanningData.amount'
        db.alter_column(u'budget_budgetplanningdata', 'amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=19, decimal_places=2))

        # Changing field 'BudgetTrackingData.term'
        db.alter_column(u'budget_budgettrackingdata', 'term', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'BudgetTrackingData.description'
        db.alter_column(u'budget_budgettrackingdata', 'description', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True))

        # Changing field 'BudgetTrackingData.label'
        db.alter_column(u'budget_budgettrackingdata', 'label', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'BudgetTrackingData.amount'
        db.alter_column(u'budget_budgettrackingdata', 'amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=19, decimal_places=2))

        # Changing field 'BudgetTrackingData.year'
        db.alter_column(u'budget_budgettrackingdata', 'year', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'BudgetUser.start_year'
        db.alter_column(u'budget_budgetuser', 'start_year', self.gf('django.db.models.fields.IntegerField')(default=1))

        # Changing field 'BudgetUser.end_year'
        db.alter_column(u'budget_budgetuser', 'end_year', self.gf('django.db.models.fields.IntegerField')(default=1))

        # Changing field 'BudgetUser.owned'
        db.alter_column(u'budget_budgetuser', 'owned', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=19, decimal_places=2))

        # Changing field 'BudgetUser.tuition'
        db.alter_column(u'budget_budgetuser', 'tuition', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=19, decimal_places=2))

        # Changing field 'BudgetUser.program_length'
        db.alter_column(u'budget_budgetuser', 'program_length', self.gf('django.db.models.fields.IntegerField')(default=1))

        # Changing field 'BudgetUser.saved'
        db.alter_column(u'budget_budgetuser', 'saved', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=19, decimal_places=2))

        # Changing field 'BudgetUser.current_year'
        db.alter_column(u'budget_budgetuser', 'current_year', self.gf('django.db.models.fields.IntegerField')(default=1))

        # Changing field 'BudgetPlanningData.term'
        db.alter_column(u'budget_budgetplanningdata', 'term', self.gf('django.db.models.fields.CharField')(default=1, max_length=2))

        # Changing field 'BudgetPlanningData.year'
        db.alter_column(u'budget_budgetplanningdata', 'year', self.gf('django.db.models.fields.IntegerField')(default=1))

        # Changing field 'BudgetPlanningData.label'
        db.alter_column(u'budget_budgetplanningdata', 'label', self.gf('django.db.models.fields.CharField')(default='fake', max_length=100))

        # Changing field 'BudgetPlanningData.amount'
        db.alter_column(u'budget_budgetplanningdata', 'amount', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=19, decimal_places=2))

        # Changing field 'BudgetTrackingData.term'
        db.alter_column(u'budget_budgettrackingdata', 'term', self.gf('django.db.models.fields.CharField')(default=1, max_length=2))

        # Changing field 'BudgetTrackingData.description'
        db.alter_column(u'budget_budgettrackingdata', 'description', self.gf('django.db.models.fields.CharField')(default='fake', max_length=2000))

        # Changing field 'BudgetTrackingData.label'
        db.alter_column(u'budget_budgettrackingdata', 'label', self.gf('django.db.models.fields.CharField')(default='fake', max_length=100))

        # Changing field 'BudgetTrackingData.amount'
        db.alter_column(u'budget_budgettrackingdata', 'amount', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=19, decimal_places=2))

        # Changing field 'BudgetTrackingData.year'
        db.alter_column(u'budget_budgettrackingdata', 'year', self.gf('django.db.models.fields.IntegerField')(default=1))

    models = {
        u'budget.budgetplanningdata': {
            'Meta': {'object_name': 'BudgetPlanningData'},
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
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
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'budget.budgetuser': {
            'Meta': {'object_name': 'BudgetUser'},
            'coop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'current_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'end_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'owned': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'program_length': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'saved': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'sequence': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tuition': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '2'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['budget']