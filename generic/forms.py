from django import forms 

class CreateNewList(forms.Form):
    name=forms.CharField(label='Full Names ',max_length=200)
    

