from django.test import TestCase

from Accounts.models import Cook
from Kitchen_app.forms import DishForm
from Kitchen_app.models import DishType


class TestKitchenForm(TestCase):
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

    def test_valid_dish_form(self):
        form_data = {
            "name": "TestDish",
            "description": "Feeeeee",
            "price": 13.99,
            "dish_type": 1,
            "cooks": [1],
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_dish_form(self):
        form_data = {
            "price": -10,
        }

        form = DishForm(data=form_data)
        self.assertTrue("price" in form.errors)
        self.assertTrue("dish_type" in form.errors)
        self.assertTrue("cooks" in form.errors)
        self.assertTrue("description" in form.errors)
        self.assertTrue("name" in form.errors)
