from django.db import models
import datetime

# Create your models here.
from faker import Faker


class Teacher(models.Model):
    Teacher_first_name = models.CharField(max_length=40, null=False)
    Teacher_second_name = models.CharField(max_length=20, null=False)
    Teacher_specializatin = models.CharField(max_length=10, null=True)
    Teacher_birthday = models.DateField(default=datetime.datetime.now().date())

    def __str__(self):
        return f'{self.Teacher_first_name}, {self.Teacher_second_name}, {self.Teacher_birthday}'

    @classmethod
    def generate_teacher(cls):
        faker=Faker()
        teacher = cls(Teacher_first_name=faker.first_name(), Teacher_second_name=faker.last_name(), Teacher_specializatin=faker.email())
        teacher.save()
        return teacher


class Groups(models.Model):
    Group_name = models.CharField(max_length=40, null=False)
    Group_specializatin = models.CharField(max_length=10, null=True)
    Group_size = models.IntegerField(max_length=3, default=0)
    Group_creation_date = models.DateField(default=datetime.datetime.now().date())

