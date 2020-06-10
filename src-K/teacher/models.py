from django.db import models
import datetime
import random
# Create your models here.
from faker import Faker


class Teacher(models.Model):
    Teacher_first_name = models.CharField(max_length=40, null=False)
    Teacher_second_name = models.CharField(max_length=20, null=False)
    Teacher_email = models.CharField(max_length=20, null=True)
    Teacher_birthday = models.DateField(default=datetime.datetime.now().date())
    Teacher_phone_number = models.CharField(max_length=16, null=True)

    def __str__(self):
        return f'{self.id},' \
            f' {self.Teacher_first_name}, ' \
            f'{self.Teacher_second_name}, ' \
            f'{self.Teacher_email}, ' \
            f'{self.Teacher_phone_number}, ' \
            f'{self.Teacher_birthday}'

    @classmethod
    def generate_teacher(cls, group=None):
        a = '+'
        for _ in range(10):
            a += str(random.randrange(0, 9, 1))
        faker = Faker()
        # if group is None:
        #     group = list(Groups.objects.all())

        teacher = cls(Teacher_first_name=faker.first_name(),
                      Teacher_second_name=faker.last_name(),
                      Teacher_email=faker.email(),
                      Teacher_phone_number=a)

        teacher.save()
        return teacher
