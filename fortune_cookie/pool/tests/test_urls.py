from django.urls import reverse, resolve

from test_plus.test import TestCase

from ..models import SeedFortune


class TestFortuneURLs(TestCase):
    """Test URL patterns for pool app."""

    def setUp(self):
        self.fortune = SeedFortune.objects.create(description="Test description")

    def test_home_reverse(self):
        self.assertEqual(reverse("home"), "/")

    def test_home_resolve(self):
        self.assertEqual(resolve("/").view_name, "home")

    def test_result_reverse(self):
        self.assertEqual(reverse("result"), "/cookie/result/")

    def test_result_resolve(self):
        self.assertEqual(resolve("/cookie/result/").view_name, "result")

    def test_change_reverse(self):
        self.assertEqual(reverse("change_fortune", args=(self.fortune.id,)),
                         "/cookie/{}/change/".format(self.fortune.id))

    def test_change_resolve(self):
        self.assertEqual(resolve("/cookie/{}/change/".format(self.fortune.id)).view_name, "change_fortune")
