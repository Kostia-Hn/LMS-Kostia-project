from django.db import models
import datetime
import random
# Create your models here.
from faker import Faker

from Group.models import Groups


class Student(models.Model):
    Student_first_name = models.CharField(max_length=40, null=False)
    Student_second_name = models.CharField(max_length=20, null=False)
    Student_email = models.EmailField(max_length=20, null=True)
    Student_birthday = models.DateField(default=datetime.date.today)
    Student_phone_number = models.CharField(max_length=16, null=True)
    Student_group = models.ForeignKey(to=Groups, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id},' \
            f' {self.Student_first_name},' \
            f' {self.Student_second_name},' \
            f' {self.Student_birthday},' \
            f' {self.Student_email},' \
            f' {self.Student_phone_number}'

    @classmethod
    def generate_student(cls):
        a = '+'
        for _ in range(10):
            a += str(random.randrange(0, 9, 1))
        faker = Faker()
        student = cls(Student_first_name=faker.first_name(),
                      Student_second_name=faker.last_name(),
                      Student_email=faker.email(),
                      Student_phone_number=a)
        student.save()
        return student
