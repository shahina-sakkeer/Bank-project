from .models import Formfill
from django import forms

class ApplicationForm(forms.ModelForm):
    class Meta:
        model=Formfill
        fields="__all__"
        
