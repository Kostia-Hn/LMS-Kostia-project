# Generated by Django 3.0.5 on 2020-05-28 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0009_auto_20200528_1555'),
        ('student', '0008_auto_20200528_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Student_group',
        ),
        migrations.AddField(
            model_name='student',
            name='Student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='Group.Groups'),
        ),
    ]
