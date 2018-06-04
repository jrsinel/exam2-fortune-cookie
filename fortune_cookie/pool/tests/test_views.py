from django.test import RequestFactory
from django.urls import reverse

from test_plus.test import TestCase

from ..models import SeedFortune
from ..views import result, FortuneUpdate


class BaseUserTestCase(TestCase):

    def setUp(self):
        self.fortune = SeedFortune.objects.create(description="Test description")
        self.factory = RequestFactory()


class TestFortuneUpdateView(BaseUserTestCase):

    def setUp(self):
        super(TestFortuneUpdateView, self).setUp()

    def test_view_url(self):
        resp = self.client.get(reverse('change_fortune', kwargs={"pk": self.fortune.id}))
        self.assertEqual(resp.status_code, 200)
