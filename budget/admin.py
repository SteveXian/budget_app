from django.contrib import admin
from budget.models import BudgetPresetData, BudgetUser, BudgetPlanningData

admin.site.register(BudgetPresetData)
admin.site.register(BudgetPlanningData)
admin.site.register(BudgetUser)