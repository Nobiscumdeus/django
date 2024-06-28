from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date', 'category', 'assigned_to']

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'datetime-local'}),
             
            'title': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500'}),
            'description': forms.Textarea(attrs={'class': 'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500'}),
            'status': forms.Select(attrs={'class': 'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500'}),
            'priority': forms.Select(attrs={'class': 'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500'}),
            'due_date': forms.DateInput(attrs={'class': 'mt-4 border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500', 'type': 'datetime-local'}),
            'category': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500'}),
            'assigned_to': forms.Select(attrs={'class': 'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500'}),
      
        }
