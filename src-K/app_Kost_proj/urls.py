"""app_Kost_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from teacher.views import generate_teachers, teachers_add, teachers_edit
from teacher.views import teachers_list

from student.views import generate_students, students_edit, students_delete
from student.views import students_add
from student.views import students_list

from Group.views import generate_groups, groups_edit
from Group.views import groups_list

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls, name='adm'),

    path('gen_teach/', generate_teachers, name='g-teach'),
    path('teachers/', teachers_list, name='teachers'),
    path('teachers/add/', teachers_add),
    path('teachers/edit/<int:id>', teachers_edit),

    path('gen_stud/', generate_students, name='g-stud'),
    path('students/', students_list, name='students'),
    path('students/add/', students_add),
    path('students/edit/<int:id>', students_edit),
    path('students/delete/<int:id>', students_delete),

    path('gen_groups/', generate_groups, name='g-grp'),
    path('groups/', groups_list, name='groups'),
    path('groups/edit/<int:id>', groups_edit),
]
