from django.test import TestCase
from django.urls import reverse


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
