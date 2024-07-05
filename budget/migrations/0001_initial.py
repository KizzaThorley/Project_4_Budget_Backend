# Generated by Django 5.0.6 on 2024-07-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('month', models.CharField(max_length=3)),
                ('year', models.FloatField()),
            ],
        ),
    ]
