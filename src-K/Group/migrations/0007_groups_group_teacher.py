# Generated by Django 3.0.5 on 2020-05-27 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0012_remove_teacher_teacher_group'),
        ('Group', '0006_auto_20200527_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='Group_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teachers', to='teacher.Teacher'),
        ),
    ]