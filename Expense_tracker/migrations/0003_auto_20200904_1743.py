# Generated by Django 3.1 on 2020-09-04 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Expense_tracker', '0002_income_outcome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='user_email',
            new_name='user',
        ),
    ]