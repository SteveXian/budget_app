from django.db import models

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
    sequence = models.CharField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def save(self):
        if self.id is None:
            self.created = datetime.today()
        self.modified = datetime.today()
        super(BudgetUser, self).save()

class BudgetData(models.Model):
    user_id = models.IntegerField(null=False)
    label = models.CharField(max_length=100)
    year = models.IntegerField()
    term = models.CharField(max_length=2, choices=TERMS)
    amount = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def save(self):
        if self.id is None:
            self.created = datetime.today()
        self.modified = datetime.today()
        super(BudgetUser, self).save()
