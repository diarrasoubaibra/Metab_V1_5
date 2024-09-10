from django import forms
from teacher.models.teacher_model import TeacherModel
from base.models.person_model import PersonModel

class TeacherFoms(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = "__all__"
        widgets={
            'birthday':forms.DateInput(attrs={'type':'date'}),
            'gender' :forms.RadioSelect(choices=PersonModel.GENDER_CHOICES),
        }