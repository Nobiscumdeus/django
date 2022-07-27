from django import forms
class StudentForm(forms.Form):
    firstname=forms.CharField(label="Enter first name",max_length=50)
    lastname=forms.CharField(label="Enter last name", max_length=100)
    
#working on form validation
from django import forms
from vote.models import Employees
class EmployeesForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields="__all__"