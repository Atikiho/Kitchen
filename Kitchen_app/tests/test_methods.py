from django.test import TestCase, Client
from django.urls import reverse

from Accounts.models import Cook
from Kitchen_app.models import DishType, Dish


class TestMethods(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(
            name="Test"
        )
        self.cook = Cook.objects.create_user(
            username="Test123",
            email="Test1234@gmail.com",
            years_of_experience=10,
            password="Test12345"
        )
        self.dish = Dish.objects.create(
            name="TestDish",
            description="Feeeeee",
            price=13.99,
            dish_type=self.dish_type,
        )
        self.dish.cooks.add(self.cook)
        self.client = Client()
        self.client.login(username="Test123", password="Test12345")

    def test_get_dish(self):
        response = self.client.get(reverse("dish-detail", kwargs={"pk": self.dish.id}))
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_dish(self):
        response = self.client.get(reverse("dish-detail", kwargs={"pk": 100001}))
        self.assertNotEqual(response.status_code, 200)

    def test_delete_dish_and_dish_type(self):
        response = self.client.post(reverse("dish-delete", kwargs={"pk": self.dish.id}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Dish.objects.filter(id=self.dish.id).exists())

        response = self.client.post(reverse("dish-type-delete", kwargs={"pk": self.dish_type.id}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(DishType.objects.filter(id=self.dish_type.id).exists())

    def test_get_dish_list(self):
        response = self.client.get(reverse("dish-list"))
        self.assertEqual(response.status_code, 200)

    def test_get_dish_type_list(self):
        response = self.client.get(reverse("dish-type-list"))
        self.assertEqual(response.status_code, 200)

