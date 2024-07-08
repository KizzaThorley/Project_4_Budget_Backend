# Generated by Django 5.0.6 on 2024-07-05 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_alter_budget_month'),
        ('expenses', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='budget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='budget.budget'),
        ),
    ]
