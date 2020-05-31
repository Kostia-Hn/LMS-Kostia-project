from django.db import models
import datetime
import random

# Create your models here.
from teacher.models import Teacher


class Classroom(models.Model):
    name = models.CharField(max_length=64)
    floor = models.SmallIntegerField(max_length=5, null=True)

    def __str__(self):
        return f'{self.name} - Floor # {self.floor}'

    @classmethod
    def generate_classroom(cls):
        clsroom = cls(name=f'Classroom - {random.choice(range(25))}',
                      floor=random.choice(range(5)))
        clsroom.save()
        return clsroom

IT_list = ['Python', 'Java', 'JS', 'SQL', 'C++', 'C#']

class Groups(models.Model):
    Group_specialization = models.CharField(max_length=10, null=True)
    Group_size = models.IntegerField(max_length=3, default=0)
    Group_creation_date = models.DateField(default=datetime.datetime.now().date())
    classroom = models.ManyToManyField(to=Classroom,
                                       null=True,
                                       related_name='groups')
    Group_teacher = models.ForeignKey(to=Teacher,
                      null=True,
                      on_delete=models.SET_NULL,
                      related_name='groups')

    def __str__(self):
        return f'{self.id},' \
            f' {self.Group_specialization},' \
            f' {self.Group_size}'

    @classmethod
    def generate_group(cls, teacher=None):
        if teacher is None:
            teacher = list(Teacher.objects.all())

        grp = cls(Group_specialization=IT_list[random.randrange(0, 5, 1)],
                  Group_size=random.randrange(15, 25, 1),
                  Group_teacher = random.choice(teacher))
        grp.save()
        return grp
