from django.contrib import admin

# Register your models here.
from teacher.models import Teacher


class TeacherAdminModel(admin.ModelAdmin):
    list_display = ('Teacher_first_name',
                    'Teacher_second_name',
                    'Teacher_email')


admin.site.register(Teacher, TeacherAdminModel)
