# Generated by Django 5.0.6 on 2024-07-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='description',
            field=models.TextField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]