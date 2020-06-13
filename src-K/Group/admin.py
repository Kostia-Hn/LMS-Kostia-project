from django.contrib import admin

# Register your models here.
from Group.models import Groups, Classroom
from student.models import Student


class StudentsInline(admin.TabularInline):
    model = Student
    readonly_fields = ('Student_birthday', 'Student_first_name', 'Student_second_name', 'Student_email')
    show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    fields = ['Group_specialization', 'classroom']
    inlines = (StudentsInline,)
    list_per_page = 10


admin.site.register(Groups, GroupAdmin)
