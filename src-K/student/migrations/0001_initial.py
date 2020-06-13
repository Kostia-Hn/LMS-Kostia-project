# Generated by Django 3.0.5 on 2020-05-13 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_first_name', models.CharField(max_length=40)),
                ('Student_second_name', models.CharField(max_length=20)),
                ('Student_email', models.CharField(max_length=15, null=True)),
                ('Student_birthday', models.DateField(default=datetime.date(2020, 5, 13))),
            ],
        ),
    ]