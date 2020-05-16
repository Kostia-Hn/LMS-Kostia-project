# Generated by Django 3.0.5 on 2020-05-16 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Student_birthday',
            field=models.DateField(default=datetime.date(2020, 5, 16)),
        ),
        migrations.AlterField(
            model_name='student',
            name='Student_email',
            field=models.EmailField(max_length=15, null=True),
        ),
    ]
