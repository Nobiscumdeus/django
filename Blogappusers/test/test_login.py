from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User=get_user_model()

class LoginTest(TestCase):
    def setUp(self):
        self.username="Esther123"
        self.email="testuser@gmail.com"
        self.password="test45####"
        
        User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )
    def test_login_exists(self):
        response=self.client.get(reverse('login_page'))
        self.assertEqual(response.statusCode,HTTPStatus.OK)
        self.assertTemplateUsed(response,'accounts/login.html')
        
    def test_login_page_has_form(self):
        response=self.client.get(reverse('login_page'))
        
        form=response.context.get('form')
        self.assertIsInstance(form,AuthenticationForm)
        
    def test_login_page_logs_in_user(self):
        user_data= {
            'username':self.username,
            'password':self.password 
        }
        response=self.client.post(reverse('login_page'),user_data)
        
        self.assertRedirects(response,reverse('homepage'))
        