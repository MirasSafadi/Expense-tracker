from django.contrib import admin
from Expense_tracker import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Income)
admin.site.register(models.Outcome)