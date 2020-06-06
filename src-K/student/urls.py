from django.urls import path

from student.views import generate_students, StudentListView, StudentUpdateView, \
    StudentCreateView, StudentDeleteView

app_name = 'students'

urlpatterns = [

    path('gen_stud/', generate_students, name='g-stud'),

    # path('', students_list, name='list'),
    path('', StudentListView.as_view(), name='list'),

    # path('add/', students_add, name='add'),
    path('add/', StudentCreateView.as_view(), name='add'),

    # path('edit/<int:id>', students_edit, name='edit'),
    path('edit/<int:pk>', StudentUpdateView.as_view(), name='edit'),

    # path('delete/<int:id>', students_delete, name='delete'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='delete'),
]
