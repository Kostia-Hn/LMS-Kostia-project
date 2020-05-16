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

def teachers_list(request):

    qs=Teacher.objects.all()

    if request.GET.get('fname'):
        qs=qs.filter(Teacher_first_name=request.GET.get('fname'))

    if request.GET.get('lname'):
        qs=qs.filter(Teacher_second_name=request.GET.get('lname'))

    result = '<br>'.join(str(Teacher) for Teacher in qs)

    return render(request=request, template_name='teachers_list.html', context={'teachers_list': result})
