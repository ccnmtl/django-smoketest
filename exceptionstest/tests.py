from django.conf import settings
from django.test import TestCase
from django.test.client import Client

from exceptionstest import EXC_MSG



class ExceptionsTest(TestCase):
    """ Check how smoke test works with different exceptionstest raise from
    different places in code.

    """
    def setUp(self):
        settings.INSTALLED_APPS = ('exceptionstest', 'smoketest')
        self.c = Client()


    def test_exceptions(self):
        response = self.c.get("/smoketest/")
        self.assertEqual(response.status_code, 500)
        self.assertIn("FAIL", response.content)
        self.assertIn(
                "Exception while importing smoke test script: %s" % EXC_MSG,
                response.content)
