from django.db import models
from datetime import datetime

SPRING = 'S'
FALL = 'F'
WINTER = 'W'
TERMS = (
    (SPRING, 'Spring'),
    (FALL, 'Fall'),
    (WINTER, 'Winter'),
)

class BudgetUser(models.Model):
    user_id = models.IntegerField(null=False)
    start_year = models.IntegerField(null=True)
    end_year = models.IntegerField(null=True)
    tuition = models.DecimalField(max_digits=19, decimal_places=2,null=True)
    saved = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    part_time = models.DecimalField(max_digits=19, decimal_places=2,null=True)
    owned = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    current_term = models.IntegerField()
    program_length = models.IntegerField(null=True)
    current_year = models.IntegerField(null=True)
    coop = models.BooleanField()
    sequence = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def save(self):
        if self.id is None:
            self.created = datetime.today()
        self.modified = datetime.today()
        super(BudgetUser, self).save()

    def __unicode__( self ):
        return "User {0}".format( str(self.user_id) )

class BudgetPlanningData(models.Model):
    user_id = models.IntegerField(null=False)
    label = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)
    term = models.CharField(max_length=2, choices=TERMS, null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    income = models.BooleanField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def save(self):
        if self.id is None:
            self.created = datetime.today()
        self.modified = datetime.today()
        super(BudgetPlanningData, self).save()

    def __unicode__(self):
        return "user {0} {1}: year {2} {3}".format( self.user_id, self.label, self.year, self.amount )

class BudgetPresetData(models.Model):
    program = models.CharField(max_length=100, null=False)
    label = models.CharField(max_length=100)
    year = models.IntegerField()
    income = models.BooleanField(null=False)
    coop = models.BooleanField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)

    def __unicode__( self ):
        return "{0} {1}: year {2} {3}".format( self.program, self.label, self.year, self.amount )

class BudgetTrackingData(models.Model):
    user_id = models.IntegerField(null=False)
    label = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=2000, null=True)
    year = models.IntegerField(null=True)
    term = models.CharField(max_length=2, choices=TERMS, null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def save(self):
        if self.id is None:
            self.created = datetime.today()
        self.modified = datetime.today()
        super(BudgetTrackingData, self).save()

    def __unicode__(self):
        return "user {0} {1} {2}: {3}".format( self.user_id, self.label, self.description, self.amount )