# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BudgetData'
        db.create_table(u'budget_budgetdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('modified', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'budget', ['BudgetData'])

        # Adding field 'BudgetUser.user_id'
        db.add_column(u'budget_budgetuser', 'user_id',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'BudgetUser.sequence'
        db.add_column(u'budget_budgetuser', 'sequence',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'BudgetUser.created'
        db.add_column(u'budget_budgetuser', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 5, 26, 0, 0)),
                      keep_default=False)

        # Adding field 'BudgetUser.modified'
        db.add_column(u'budget_budgetuser', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 5, 26, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'BudgetData'
        db.delete_table(u'budget_budgetdata')

        # Deleting field 'BudgetUser.user_id'
        db.delete_column(u'budget_budgetuser', 'user_id')

        # Deleting field 'BudgetUser.sequence'
        db.delete_column(u'budget_budgetuser', 'sequence')

        # Deleting field 'BudgetUser.created'
        db.delete_column(u'budget_budgetuser', 'created')

        # Deleting field 'BudgetUser.modified'
        db.delete_column(u'budget_budgetuser', 'modified')


    models = {
        u'budget.budgetdata': {
            'Meta': {'object_name': 'BudgetData'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
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