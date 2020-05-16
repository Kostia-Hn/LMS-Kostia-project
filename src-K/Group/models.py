from django.db import models
import datetime
import random

# Create your models here.
from faker import Faker

IT_list = ['Python', 'Java', 'JS', 'SQL', 'C++', 'C#']

class Groups(models.Model):
    Group_specialization = models.CharField(max_length=10, null=True)
    Group_size = models.IntegerField(max_length=3, default=0)
    Group_creation_date = models.DateField(default=datetime.datetime.now().date())

    def __str__(self):
        return f'{self.id}, {self.Group_specialization}, {self.Group_size}'

    @classmethod
    def generate_group(cls):
        faker=Faker()
        grp = cls(Group_specialization = IT_list[random.randrange(0,5,1)], Group_size = random.randrange(15,25,1))
        grp.save()
        return grp

