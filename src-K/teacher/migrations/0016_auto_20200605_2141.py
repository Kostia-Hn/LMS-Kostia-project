# Generated by Django 3.0.5 on 2020-06-05 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0015_auto_20200602_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Teacher_birthday',
            field=models.DateField(default=datetime.date(2020, 6, 5)),
        ),
    ]
