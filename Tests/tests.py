from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

from Kitchen_app.models import Cook, DishType


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
        self.assertTrue(self.client.login(username="Test123", password="Test12345"))

    def test_login_invalid_data(self):
        self.assertFalse(self.client.login(username="Test123", password="Test"))


class TestSearch(TestCase):
    def test_search_dish(self):

        data = {
            "name": "H",
            "price_min": 1,
            "price_max": 20,
            "dish_type": 1,
        }
        response = self.client.get(
            reverse("dish-list"),
            data,
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue("name" in response.request.get("QUERY_STRING"))
        self.assertTrue("price_min" in response.request.get("QUERY_STRING"))
        self.assertTrue("price_max" in response.request.get("QUERY_STRING"))
        self.assertTrue("dish_type" in response.request.get("QUERY_STRING"))
