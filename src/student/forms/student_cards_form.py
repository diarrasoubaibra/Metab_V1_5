from django import forms
from student.models.student_cards_model import StudentCardsModel


class StudentCardFoms(forms.ModelForm):
    class Meta:
        model = StudentCardsModel
        fields = "__all__"
        widgets={
            'issue_date':forms.DateInput(attrs={'type':'date'}),
            'expiration_date':forms.DateInput(attrs={'type':'date'}),
            
        }
       