from django import forms
from student.models.absence_model import AbsenceModel


class AbsenceFoms(forms.ModelForm):
    class Meta:
        model = AbsenceModel
        fields = "__all__"
        widgets={
            'absence_date':forms.DateInput(attrs={'type':'date'}),
        }
        