from django.test import TestCase, Client
from django.urls import reverse

from Accounts.models import Cook
from Kitchen_app.models import DishType


class TestLogin(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="Test123",
            email="Test1234@gmail.com",
            years_of_experience=10,
            password="Test12345"
        )
        self.dish_type = DishType.objects.create(
            name="Test"
        )
        self.client = Client()

    def test_login_required(self):
        urls_with_login_required = [
            "cook-delete",
            "cook-update",
            "cook-detail",
            "dish-detail",
            "dish-delete",
            "dish-type-delete",
        ]
        urls_without_pk = [
            "cook-list",
            "dish-list",
            "dish-create",
            "dish-type-create",
            "dish-type-list",
        ]
        for reversed_url, url_without_pk in zip(urls_with_login_required, urls_without_pk):
            url = self.client.get(reverse(reversed_url, kwargs={"pk": 1}))
            self.assertEqual(url.status_code, 302)
            url = self.client.get(reverse(url_without_pk))
            self.assertEqual(url.status_code, 302)

    def test_login(self):
        self.assertTrue(
            self.client.login(
                username="Test123",
                password="Test12345")
        )

    def test_login_invalid_data(self):
        self.assertFalse(
            self.client.login(
                username="Test123",
                password="Test")
        )
