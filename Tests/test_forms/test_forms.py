from django.test import TestCase

from Kitchen_app.forms import DishForm, CookForm
from Kitchen_app.models import Cook, DishType


class TestForm(TestCase):
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

    def test_valid_cook_form(self):
        form_data = {
            "username": "Test",
            "email": "Test1234@gmail.com",
            "years_of_experience": 10,
            "password1": "1qazcde123",
            "password2": "1qazcde123",
        }

        form = CookForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_dish_form(self):
        form_data = {
            "price": -10,
        }

        form = DishForm(data=form_data)
        self.assertTrue("price" in form.errors)
        self.assertTrue("dish_type" in form.errors)

    def test_invalid_cook_form(self):
        form_data = {
            "username": "Test123",
            "email": "Test1234",
            "years_of_experience": -10,
            "password1": "1qazcde12",
            "password2": "1qazcde123",
        }

        form = CookForm(data=form_data)
        self.assertTrue("email" in form.errors)
        self.assertTrue("username" in form.errors)
        self.assertTrue("username" in form.errors)
        self.assertTrue("years_of_experience" in form.errors)
