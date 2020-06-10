from django.core.exceptions import ValidationError
from django.forms import ModelForm

from student.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAddForm(StudentBaseForm):
    pass


class StudentEditForm(StudentBaseForm):

    def clean_Student_email(self):
        email = self.cleaned_data['Student_email']
        filt_stud_qs = Student.objects.all().filter(Student_email=email)

        if len(filt_stud_qs) > 0 and not filt_stud_qs[0].id == self.instance.id:
            raise ValidationError("This e-mail exists")

        return email

    def clean_Student_first_name(self):
        f_name = self.cleaned_data['Student_first_name']
        filt_stud_qs = Student.objects.all().filter(Student_second_name=f_name)

        for i in filt_stud_qs:
            if i.id == self.instance.id:
                raise ValidationError("First name "
                                      "cannot be the same as the second name")

        return f_name

    def clean_Student_second_name(self):
        s_name = self.cleaned_data['Student_second_name']
        filt_stud_qs = Student.objects.all().filter(Student_first_name=s_name)

        for i in filt_stud_qs:
            if i.id == self.instance.id:
                raise ValidationError("Second name "
                                      "cannot be the same as the first name")

        return s_name
