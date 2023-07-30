from django.test import TestCase
from django.urls import reverse 
from http import HttpStatus
from django.contrib.auth.forms import UserCreationForm
from ..forms import UserRegistrationForm #or from Blogappusers.forms import UserRegistrationForm
from django.contrib.auth import get_user_model


User=get_user_model()
# Create your tests here.
class AccountCreationTest(TestCase): 
    def setUp(self)->None:
        self.form_class=UserRegistrationForm()
    def test_signup_page_exits(self):
        response=self.client.get(reverse('signup_page'))
        self.assertEqual(response.statusCode,HttpStatus.OK)
        self.assertTemplateUsed('accounts/register.html')
        self.assertContains(response,"Create your account today")
    
    def test_signup_page_works_correctly(self):
        form=self.form_class()
        self.assertTrue(issubclass(self.form_class,UserCreationForm))
        self.assertTrue('email' in self.form_class.Meta.fields)
        self.assertTrue('username' in self.form_class.Meta.fields)
        self.assertTrue('password1' in self.form_class.Meta.fields)
        self.assertTrue('password2' in self.form_class.Meta.fields)
        
        sample_data={
            "email":"test@test.com",
            "username":"test",
            "password1":"test123###",
            "password20":"test123###"
        }
        form=self.form_class(sample_data)
        self.assertTrue(form.is_valid())
        
    def test_signup_form_creates_user_in_db(self):
        user={
            "email":"test@test.com",
            "username":"test",
            "password1":"test123###",
            "password20":"test123###"
        }
        form=self.form_class(user)
        if form.is_valid():
            form.save()
            
        self.assertEqual(User.objects.count(),1)