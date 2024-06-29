from django import forms
from .models import Task
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm,UserCreationForm
from django.contrib.auth.models import User


class UsersCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password1','password2')
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        #Apply Bootstrap classes , placeholders and other attributes 
        field_classes={
            'first_name':'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500',
            'last_name':'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500',
            'username':'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500',
            'email':'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500',
            'password1':'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500',
            'password2':'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500',
           
        }
        field_placeholder={
            'first_name':'Enter your first name',
            'last_name':'Enter your Surname',
            'username':'Please Enter your Names',
            'email':'Enter your Email address',
            'password1':'Enter your password',
            'password2':'Confirm your Password',
          
        }
        field_attributes={
            'username':{'type':'text','data-required':'true'},
            'email':{'type':'email'},
            'password1':{'type':'password','data-strength-meter':'true'},
            'password2':{'type':'password','data-strength-meter':'true'},
            
            
            
            #for birth 'birth':{'class':'datepicker','data-datepicker-options':'{"format":"dd/mm/yyyy"}'}
            
        }
        for field_name,css_class in field_classes.items():
            self.fields[field_name].widget.attrs['class']=css_class
            
        for field_name,placeholder_text in field_placeholder.items():
            self.fields[field_name].widget.attrs['placeholder']=placeholder_text
        
        for field_name,attributes in field_attributes.items():
            self.fields[field_name].widget.attrs.update(attributes)
        
class UserLoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #Remove fields other than username and password
        for field_name in self.fields:
            if field_name not in ['username','password']:
                self.fields.pop(field_name)  
        field_classes={
            'username':'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500',
            'password':'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500'
            }
        field_placeholder={
            
        
            'username':'Please Enter your Username',
            'password':'Please, Input your password'
        }
        for field_name,css_class in field_classes.items():
            self.fields[field_name].widget.attrs['class']=css_class
            
        for field_name,placeholder_text in field_placeholder.items():
            self.fields[field_name].widget.attrs['placeholder']=placeholder_text
            
        
        
    class Meta:
        model=User
        
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
        
        

class EditTaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','description','priority','due_date','category','assigned_to']
        
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'datetime-local'}),  
            'title': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500'}),
            'description': forms.Textarea(attrs={'class': 'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500'}),
            
            'priority': forms.Select(attrs={'class': 'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500'}),
            'due_date': forms.DateInput(attrs={'class': 'mt-4 border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500', 'type': 'datetime-local'}),
            'category': forms.TextInput(attrs={'class': 'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500'}),
            'assigned_to': forms.Select(attrs={'class': 'border border-gray-300 rounded-lg px-3 py-2 w-full focus:outline-none focus:border-blue-500'}),
      
        }
        


#### A search form 


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}))
    sort_by = forms.ChoiceField(choices=[
        ('title', 'Title'),
        ('due_date', 'Due Date'),
        ('priority', 'Priority'),
    ], required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    status = forms.ChoiceField(choices=[
        ('', 'Any'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue')
    ], required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    priority = forms.ChoiceField(choices=[
        ('', 'Any'),
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], required=False, widget=forms.Select(attrs={'class': 'form-select'}))
