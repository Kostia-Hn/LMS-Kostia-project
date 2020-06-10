from django.urls import path

from teacher.views import generate_teachers, TeacherListView, TeacherCreateView, \
    TeacherUpdateView

app_name = 'teachers'

urlpatterns = [
    path('gen_teach/', generate_teachers, name='g-teach'),


    # path('', teachers_list, name='teachers'),
    path('', TeacherListView.as_view(), name='list'),

    # path('add/', teachers_add),
    path('add/', TeacherCreateView.as_view(), name='add'),

    # path('edit/<int:id>', teachers_edit, name='edit'),
    path('edit/<int:pk>', TeacherUpdateView.as_view(), name='edit'),

]
