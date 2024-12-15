from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from Accounts.models import Cook


class TestMethods(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="Test123",
            email="Test1234@gmail.com",
            years_of_experience=10,
            password="Test12345"
        )
        self.client = Client()
        self.client.login(username="Test123", password="Test12345")

    def test_get_cook(self):
        response = self.client.get(reverse("cook-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_cook(self):
        response = self.client.get(reverse("cook-detail", kwargs={"pk": 100001}))
        self.assertNotEqual(response.status_code, 200)

    def test_get_cook_list(self):
        response = self.client.get(reverse("cook-list"))
        self.assertEqual(response.status_code, 200)

    def test_delete_cook(self):
        response = self.client.post(reverse("cook-delete", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(get_user_model().objects.filter(id=1).exists())
