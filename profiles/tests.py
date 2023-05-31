from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from rest_framework import status
from rest_framework.test import APIClient


class ProfilesTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = RequestFactory()
        self.register_url = reverse('register')
        self.login_url = reverse('token_create')
        self.logout_url = reverse('logout')
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_register_user(self):
        data = {
            'username': 'newuser',
            'password': 'newpassword'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)

    def test_register_user_missing_fields(self):
        data = {
            'username': 'newuser'
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user(self):
        data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)

    def test_get_username(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('get_username'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.username)
