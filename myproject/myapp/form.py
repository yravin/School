from django import forms
from .models import Teacher, Schedule

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
