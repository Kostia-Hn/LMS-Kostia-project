from django.core.management.base import BaseCommand

from Group.models import Groups
from student.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):

        Student.objects.all().delete()
        group = list(Groups.objects.all())
        quantity = args[0]
        if quantity > 200:
            quantity = 5
        print(f'Generating {quantity} students:')
        lst = []
        for _ in range(quantity):
            a = Student.generate_student(group)
            lst.append(a)
        for teach in lst:
            print(teach.Student_first_name, " ", teach.Student_second_name)

    def add_arguments(self, parser):
        parser.add_argument(nargs='+', type=int, dest='args')
