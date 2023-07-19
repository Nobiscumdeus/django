from django.forms import ModelForm
from django import forms
from .models import Reporter


class ReporterForm(ModelForm):
    full_name=forms.TextInput()
    class Meta:
        model=Reporter
        fields=['full_name']
    