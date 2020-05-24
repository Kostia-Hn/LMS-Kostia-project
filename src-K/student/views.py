from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse

from student.forms import StudentAddForm, StudentEditForm
from student.models import Student
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


# Create your views here.
def generate_students(request):
    amount = int(request.GET['amount'])
    lst = []
    if amount > 200:
        amount = 5
    for _ in range(amount):
        a = Student.generate_student()
        lst.append(a.Student_first_name)
        lst.append('<br>')
    return HttpResponse(f'generated {amount} students: <br> {lst}')

def students_list(request):

    qs = Student.objects.all()
    if request.GET.get('fname'):
        qs = qs.filter(Student_first_name=request.GET.get('fname'))
    if request.GET.get('lname'):
        qs = qs.filter(Student_second_name=request.GET.get('lname'))
    if request.GET.get('tname'):
        qs = qs.filter(Student_email=request.GET.get('tname'))

    return render(request=request,
                  template_name='students_list.html',
                  context={'students_list': qs})

def students_add(request):

    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            qs_2 = Student.objects.all()
            qs_3 = qs_2.filter(Student_email=request.POST['Student_email'])
            qs_4 = qs_2.filter(Student_phone_number=request.POST['Student_phone_number'])
            if len(qs_3) > 0:
                return HttpResponse('This e-mail already exists')
            elif len(qs_4) > 0:
                return HttpResponse('This phone number already exists')
            else:
                form.save()
                return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentAddForm()

    return render(request=request,
                  template_name='students_add.html',
                  context={'form': form,
                           'title': 'Student_edt'})

def students_edit(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Student with id={id} not found, sorry')

    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentEditForm(
            instance=student
        )

    return render(request=request,
                  template_name='students_edit.html',
                  context={'form': form,
                  'title': 'Student_edit'})

def students_delete(request, id):
    student = Student.objects.get(id=id)
    name = student.Student_first_name
    sname = student.Student_second_name
    student.delete()
    return HttpResponse(f'Student {name} {sname} deleted')
