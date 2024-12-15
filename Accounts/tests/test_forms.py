from django.test import TestCase

from Accounts.forms import CookForm
from Accounts.models import Cook


class TestUserForm(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="Test123",
            email="Test1234@gmail.com",
            years_of_experience=10,
            password="Test12345"
        )

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
        self.assertTrue("years_of_experience" in form.errors)
