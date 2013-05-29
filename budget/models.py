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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    program = models.CharField(max_length=500)
    program_length = models.IntegerField()
    current_year = models.IntegerField()
    coop = models.BooleanField()
    sequence = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def save(self):
        if self.id is None:
            self.created = datetime.today()
        self.modified = datetime.today()
        super(BudgetUser, self).save()

class BudgetPlanningData(models.Model):
    user_id = models.IntegerField(null=False)
    label = models.CharField(max_length=100)
    year = models.IntegerField()
    term = models.CharField(max_length=2, choices=TERMS)
    amount = models.DecimalField(max_digits=19, decimal_places=10)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def save(self):
        if self.id is None:
            self.created = datetime.today()
        self.modified = datetime.today()
        super(BudgetPlanningData, self).save()
