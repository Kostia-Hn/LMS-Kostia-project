from django.core.management.base import BaseCommand
from teacher.models import Teacher

class Command(BaseCommand):

    def handle(self, *args, **options):
        quantity = args[0]
        if quantity > 200:
            quantity = 5
        print(f'Generating {quantity} teachers:')
        lst = []
        for _ in range(quantity):
            a = Teacher.generate_teacher()
            lst.append(a)
        for teach in lst:
            print(teach.Teacher_first_name, " ", teach.Teacher_second_name)

    def add_arguments(self, parser):
        parser.add_argument(nargs='+', type=int, dest='args')
