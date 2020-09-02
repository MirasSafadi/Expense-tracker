# Generated by Django 3.1 on 2020-09-02 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Expense_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('isPeriodic', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Expense_tracker.user')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('isPeriodic', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Expense_tracker.user')),
            ],
        ),
    ]
