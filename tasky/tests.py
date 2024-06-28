from django.test import TestCase


from django.contrib.auth.models import User
from .models import Task
from django.urls import reverse


'''
First, we’ll create tests for the Task model to ensure 
that tasks are created correctly and the string representation works.
'''
class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            due_date='2024-07-01 12:00',
            completed=False,
            user=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(self.task.completed, False)
        self.assertEqual(self.task.user.username, 'testuser')

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Test Task')


'''
 we’ll create tests for your views, ensuring that they 
 respond correctly and that templates are rendered as expected.
'''
class TaskListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            due_date='2024-07-01 12:00',
            completed=False,
            user=self.user
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasky/task_list.html')
        self.assertContains(response, 'Test Task')


####Testing Create View 
class TaskCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_task_create_view(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'New Description',
            'due_date': '2024-07-01 12:00',
            'completed': False
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.last().title, 'New Task')

### Test Update View 
class TaskUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            due_date='2024-07-01 12:00',
            completed=False,
            user=self.user
        )

    def test_task_update_view(self):
        response = self.client.post(reverse('task_update', args=[self.task.id]), {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'due_date': '2024-07-01 12:00',
            'completed': False
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')



#### test Delete View
class TaskDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            due_date='2024-07-01 12:00',
            completed=False,
            user=self.user
        )

    def test_task_delete_view(self):
        response = self.client.post(reverse('task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())



#### Tests for our urls
from django.urls import reverse, resolve
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

class TaskURLTest(TestCase):
    def test_task_list_url(self):
        url = reverse('task_list')
        self.assertEqual(resolve(url).func.view_class, TaskListView)

    def test_task_create_url(self):
        url = reverse('task_create')
        self.assertEqual(resolve(url).func.view_class, TaskCreateView)

    def test_task_update_url(self):
        url = reverse('task_update', args=[1])
        self.assertEqual(resolve(url).func.view_class, TaskUpdateView)

    def test_task_delete_url(self):
        url = reverse('task_delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, TaskDeleteView)
