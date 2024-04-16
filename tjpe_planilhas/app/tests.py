# tests.py
from django.test import TestCase, Client
from django.contrib.auth.models import User

class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login(self):
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json())

    def test_login_wrong_credentials(self):
        response = self.client.post('/login/', {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 400)