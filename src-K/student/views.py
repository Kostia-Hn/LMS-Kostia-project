
from django.shortcuts import render
from student.models import Student
from django.http import HttpResponse

# Create your views here.
def generate_students(request):
    amount = int(request.GET['amount'])
    lst=[]
    if amount > 200:
        amount = 5
    for _ in range(amount):
        a = Student.generate_student()
        lst.append(a.Student_first_name)
        lst.append('<br>')
    return HttpResponse(f'generated {amount} students: <br> {lst}')

def students_list(request):

    qs=Student.objects.all()

    if request.GET.get('fname'):
        qs=qs.filter(Student_first_name=request.GET.get('fname'))

    if request.GET.get('lname'):
        qs=qs.filter(Student_second_name=request.GET.get('lname'))

    if request.GET.get('tname'):
        qs = qs.filter(Student_email=request.GET.get('tname'))


    result = '<br>'.join(str(Student) for Student in qs)

    return render(request=request, template_name='students_list.html', context={'students_list': result})
