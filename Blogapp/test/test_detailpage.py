from django.test import TestCase
from Blogapp.models import Post 
from django.contrib.auth import get_user_model
from http import HTTPStatus
from model_bakery import baker


class DetailPageTest(TestCase):
    def setUp(self)->None:
        post=baker.make(Post)
        
        def test_detail_page_returns_correct_response(self):
            self.client.defaults['SERVER_NAME'] = 'localhost'  # Set the desired domain
            self.client.defaults['SERVER_PORT'] = '8000'  # Set the desired port
            response=self.client.get(post.get_absolute_url())
            self.assertEqual(response.status_code,HTTPStatus.OK)
            self.assertTemplateUsed(response,'blogapp/detail.html')
        def test_detail_page_returns_correct_content(self):
            response=self.client.get(self.post.get_absolute_url())
            self.assertContains(response,post.title)
            self.assertContains(response,post.body)
            self.assertContains(response,post.created_at)