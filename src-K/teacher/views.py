from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView

from teacher.forms import TeacherAddForm, TeacherEditForm
from teacher.models import Teacher
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


# Create your views here.

def generate_teachers(request):
    amount = int(request.GET['amount'])
    lst = []
    if amount > 200:
        amount = 5
    for _ in range(amount):
        a = Teacher.generate_teacher()
        lst.append(a.Teacher_first_name)
        lst.append('<br>')
    return HttpResponse(f'generated {amount} teachers: <br> {lst}')

# def teachers_list(request):
#
#     qs = Teacher.objects.all()
#
#     if request.GET.get('fname'):
#         qs = qs.filter(Teacher_first_name=request.GET.get('fname'))
#
#     if request.GET.get('lname'):
#         qs = qs.filter(Teacher_second_name=request.GET.get('lname'))
#
#     return render(request=request,
#                   template_name='teachers_list.html',
#                   context={'teachers_list': qs})
#
# def teachers_add(request):
#
#     if request.method == 'POST':
#         form = TeacherAddForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers'))
#     else:
#         form = TeacherAddForm()
#
#     return render(request=request, template_name='teachers_add.html', context={'form': form})
#
# def teachers_edit(request, id):
#     try:
#         teacher = Teacher.objects.get(id=id)
#     except ObjectDoesNotExist:
#         return HttpResponseNotFound(f'Teacher with id={id} not found, sorry')
#
#     if request.method == 'POST':
#         form = TeacherEditForm(request.POST, instance=teacher)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('teachers:list'))
#     else:
#         form = TeacherEditForm(
#             instance=teacher
#         )
#
#     return render(request=request,
#                   template_name='teachers_edit.html',
#                   context={'form': form,
#                   'title': 'Teacher_edit',
#                   'teachers': teacher})
#

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers_list.html'
    context_object_name = 'teachers_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Teachers list'
        return context

class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers_edit.html'
    form_class = TeacherEditForm

    def get_success_url(self):
        return reverse('teachers:list')

class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'students_add.html'
    form_class = TeacherAddForm

    def get_success_url(self):
        return reverse('teachers:list')
