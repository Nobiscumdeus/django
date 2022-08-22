from django import forms
from Todo.models import Student
from Todo.models import Validation

class EmpForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

class StudentForm(forms.Form):
    firstname=forms.CharField(label="Enter First Name",max_length=30)
    lastname=forms.CharField(label="Enter Last Name",max_length=30)
    email=forms.EmailField(label="Enter Email")
    file=forms.FileField() #for creating file input
    
class ValidationForm(forms.ModelForm):
    class Meta:
        model=Validation
        fields="__all__"
