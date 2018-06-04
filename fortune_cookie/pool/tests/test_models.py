from test_plus.test import TestCase

from ..models import SeedFortune


class TestFortune(TestCase):

    def setUp(self):
        self.fortune = SeedFortune.objects.create(description="Test description")

    def test__str__(self):
        self.assertEqual(
            self.fortune.__str__(),
            "Test description"
        )
