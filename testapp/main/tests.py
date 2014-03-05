import simplejson

from django.test import TestCase
from django.test.client import Client

from smoke import TestFailedSmokeTests



class BasicTest(TestCase):
    def setUp(self):
        self.c = Client()


    def test_basics(self):
        response = self.c.get("/smoketest/")
        self.assertEqual(response.status_code, 200)

        self.assertIn("FAIL", response.content)
        # only tests from TestFailedSmokeTests should fail
        self.assertNotIn(".SmokeTest.", response.content)
        # and both tests from TestFailedSmokeTests should fail
        self.assertIn("tests failed: 2\n", response.content)
        self.assertIn("tests errored: 0\n", response.content)
        self.assertIn(
                ".TestFailedSmokeTests.test_assertTrueWoMsg failed: False is not true",
                response.content)
        self.assertIn(
                ".TestFailedSmokeTests.test_assertEqualWMsg failed: %s" %
                        TestFailedSmokeTests.CUSTOM_TEST_MSG,
                response.content)


    def test_json(self):
        " Testing JSON response. "
        json_content_type = 'application/json'
        response = self.c.get("/smoketest/", HTTP_ACCEPT=json_content_type)
        self.assertEqual(json_content_type, response.get('Content-Type', None))

        response_obj = simplejson.loads(response.content)
        self.assertEqual('FAIL', response_obj['status'])
        self.assertEqual(2, response_obj['tests_failed'])
        self.assertEqual(0, response_obj['tests_errored'])
        # just in case, check the length of arrays also
        self.assertEqual(
                response_obj['tests_failed'], len(response_obj['failed_tests']))
        self.assertEqual(
                response_obj['tests_errored'],
                len(response_obj['errored_tests']))
        self.assertIn(
                "main.smoke.TestFailedSmokeTests.test_assertTrueWoMsg failed: False is not true",
                response_obj['failed_tests'])
        self.assertIn(
                "main.smoke.TestFailedSmokeTests.test_assertEqualWMsg failed: %s" %
                        TestFailedSmokeTests.CUSTOM_TEST_MSG,
                response_obj['failed_tests'])
