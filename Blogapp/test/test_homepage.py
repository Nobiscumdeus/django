from django.test import TestCase
from Blogapp.models import Post 
from django.contrib.auth import get_user_model



from http import HTTPStatus
from model_bakery import baker

# Create your tests here.
User=get_user_model()  #i.e Our user module is equal to the model coming from django 
class PostModelTests(TestCase):
    def test_post_model_exits(self):
        posts=Post.objects.count()
        
        self.assertEqual(posts,0)
        
   
        

class PostAuthorTest(TestCase):
    def setUp(self)->None:
       self.user=baker.make(User)
       self.post=Post.objects.create(
           title="Test title",
           body="Test body",
           author=self.user
       )
    def test_author_is_instance_of_user_model(self):
        self.assertTrue(isinstance(self.user,User))
        
    def test_post_belongs_to_user(self):
        self.assertTrue(hasattr(self.post,'author'))
        self.assertEqual(self.post.author,self.user)
        

        
        



