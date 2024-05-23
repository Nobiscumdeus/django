from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=('username','email','password1','password2')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        field_classes={
            
                'username':'mt-2 block w-full text-2xl font-bold border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm p-3 font-bold text-black ',
                'email':'mt-2 block w-full text-2xl font-bold border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm p-3 font-bold text-black',
                'password1':'mt-2 block w-full text-2xl font-bold border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm p-3 font-bold text-black',
                'password2':'mt-2 block w-full text-2xl font-bold border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm p-3 font-bold text-black',
                
            }
        field_placeholder={
            
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
            'username':'mt-2 block w-full text-3xl font-bold border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm p-3 font-bold text-black',
            'password':'mt-2 block w-full text-3xl font-bold border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm p-3 font-bold text-black'
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
    

#API View for Sensor Datafrom django.shortcuts import render

# Create your views here.

#API View for Sensor Data