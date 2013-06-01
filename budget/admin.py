from django.contrib import admin
from budget.models import BudgetPresetData, BudgetUser, BudgetPlanningData, BudgetTrackingData

admin.site.register(BudgetPresetData)
admin.site.register(BudgetPlanningData)
admin.site.register(BudgetUser)
admin.site.register(BudgetTrackingData)