# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BudgetData.amount'
        db.alter_column(u'budget_budgetdata', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=10))

    def backwards(self, orm):

        # Changing field 'BudgetData.amount'
        db.alter_column(u'budget_budgetdata', 'amount', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'budget.budgetdata': {
            'Meta': {'object_name': 'BudgetData'},
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