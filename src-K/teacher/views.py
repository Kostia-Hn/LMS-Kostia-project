from django.shortcuts import render
from teacher.models import Teacher
from django.http import HttpResponse
# Create your views here.

def generate_teachers(request):
    amount = int(request.GET['amount'])
    lst=[]
    if amount > 200:
        amount = 5
    for _ in range(amount):
        a = Teacher.generate_teacher()
        lst.append(a.Teacher_first_name)
        lst.append('<br>')
    return HttpResponse(f'generated {amount} teachers: <br> {lst}')