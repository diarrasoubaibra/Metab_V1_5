from django import forms
from user.models.role_user_model import RoleUserModel


class RoleUserFoms(forms.ModelForm):
    class Meta:
        model = RoleUserModel
        fields = "__all__"
        