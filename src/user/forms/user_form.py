from django import forms
from user.models.user_model import UserModel


class UserFoms(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['school', 'role', 'pseudo', 'password']

        password = forms.CharField(widget=forms.PasswordInput)
        