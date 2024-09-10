from django import forms
from student.models.student_model import StudentModel
from base.models.person_model import PersonModel

class StudentFoms(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
        widgets={
            'birthday':forms.DateInput(attrs={'type':'date'}),
            'gender' :forms.RadioSelect(choices=PersonModel.GENDER_CHOICES),
        }
