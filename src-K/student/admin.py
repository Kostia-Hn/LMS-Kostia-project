from django.contrib import admin

# Register your models here.
from student.models import Student


class StudentAdminModel(admin.ModelAdmin):
    list_display = ('Student_first_name',
                    'Student_second_name',
                    'Student_email',
                    'Student_group')
    list_select_related = ('Student_group',)


admin.site.register(Student, StudentAdminModel)
