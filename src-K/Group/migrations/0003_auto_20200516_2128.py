# Generated by Django 3.0.5 on 2020-05-16 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0002_auto_20200513_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='Group_creation_date',
            field=models.DateField(default=datetime.date(2020, 5, 16)),
        ),
    ]