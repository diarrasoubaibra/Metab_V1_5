from django import forms
from school.models.app_setting_model import AppSettingsModel


class AppSettingFoms(forms.ModelForm):
    class Meta:
        model = AppSettingsModel
        fields = "__all__"
        