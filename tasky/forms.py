from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date', 'category', 'assigned_to']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'datetime-local'}),
             
            'title': forms.TextInput(attrs={'class': 'px-4 py-2 border rounded-md'}),
            'description': forms.Textarea(attrs={'class': 'px-4 py-2 border rounded-md'}),
            'status': forms.Select(attrs={'class': 'px-4 py-2 border rounded-md'}),
            'priority': forms.Select(attrs={'class': 'px-4 py-2 border rounded-md'}),
            'due_date': forms.DateInput(attrs={'class': 'px-4 py-2 border rounded-md', 'type': 'datetime-local'}),
            'category': forms.TextInput(attrs={'class': 'px-4 py-2 border rounded-md'}),
            'assigned_to': forms.Select(attrs={'class': 'px-4 py-2 border rounded-md'}),
      
        }
