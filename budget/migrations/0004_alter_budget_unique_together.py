# Generated by Django 5.0.6 on 2024-07-05 09:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_alter_budget_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='budget',
            unique_together={('month', 'year', 'owner')},
        ),
    ]
