# Generated by Django 2.2.7 on 2019-11-14 03:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='birthday',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
