from django import forms
from .models.address_model import AddressModel

class AdressFoms(forms.ModelForm):
    class Meta:
        model = AddressModel
        fields = "__all__"
        