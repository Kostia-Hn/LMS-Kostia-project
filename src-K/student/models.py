from django.db import models
import datetime

# Create your models here.
from faker import Faker


class Student(models.Model):
    Student_first_name = models.CharField(max_length=40, null=False)
    Student_second_name = models.CharField(max_length=20, null=False)
    Student_email = models.CharField(max_length=15, null=True)
    Student_birthday = models.DateField(default=datetime.datetime.now().date())

    def __str__(self):
        return f'{self.id}, {self.Student_first_name}, {self.Student_second_name}, {self.Student_email}'

    @classmethod
    def generate_student(cls):
        faker=Faker()
        student = cls(Student_first_name=faker.first_name(), Student_second_name=faker.last_name(), Student_email=faker.email())
        student.save()
        return student