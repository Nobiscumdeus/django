from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        '''
        was published recently should return false for questions published in the future
        '''
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=Question(date_published=time)
        self.assertIs(future_question.was_published_recently(),False)
    def test_was_published_recently_with_old_question(self):
        '''
        we want this to return false for question older than 1 day
        '''
        time=timezone.now()-datetime.timedelta(days=1,seconds=1)
        old_question=Question(date_published=time)
        self.assertIs(future_question.was_published_recently(),False)
        
def create_question(question_text,days):
    time=timezone.now()+datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,date_published=days)

#Creating a test for the indexview
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If no question exists, then an appropriate message is relayed 
        """
        response=self.client.get(reverse('generic:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
   
        
        