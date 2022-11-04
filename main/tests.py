import json

from django.conf import settings
from django.test import TestCase
from django.test.client import Client

from .smoke import TestFailedSmokeTests
from smoketest import SmokeTest


class BasicTest(TestCase):

    _EXC_MSG = 'test exception'
    _FAIL_MSG = 'some other fail test message'

    class TestWithException(SmokeTest):
        def test_fail(self):
            self.assertTrue(False, BasicTest._FAIL_MSG)

        def test_with_exception(self):
            raise Exception(BasicTest._EXC_MSG)

        def dir(self):
            """ Overvrite dir method so test_fail would be before
            test_with_exception for sure.

            """
            return ['test_fail', 'test_with_exception']

    def setUp(self):
        settings.INSTALLED_APPS = ('main', 'smoketest')
        self.c = Client()

    def test_basics(self):
        response = self.c.get("/smoketest/")
        self.assertEqual(500, response.status_code)

        self.assertIn("FAIL", response.content.decode('utf-8'))
        # only tests from TestFailedSmokeTests should fail
        self.assertNotIn(".SmokeTest.",
                         response.content.decode('utf-8'))
        # and both tests from TestFailedSmokeTests should fail
        self.assertIn("tests failed: 2\n",
                      response.content.decode('utf-8'))
        self.assertIn("tests errored: 0\n",
                      response.content.decode('utf-8'))
        self.assertIn(
            (".TestFailedSmokeTests.test_assertTrueWoMsg "
             "failed: False is not true"),
            response.content.decode('utf-8'))
        self.assertIn(
            ".TestFailedSmokeTests.test_assertEqualWMsg failed: %s" %
            TestFailedSmokeTests.CUSTOM_TEST_MSG,
            response.content.decode('utf-8'))

    def test_extendable(self):
        response = self.c.get("/extendable/")
        self.assertEqual(500, response.status_code)

    def test_json(self):
        " Testing JSON response. "
        json_content_type = 'application/json'
        response = self.c.get("/smoketest/", HTTP_ACCEPT=json_content_type)
        self.assertEqual(500, response.status_code)
        self.assertEqual(json_content_type, response.get('Content-Type', None))

        response_obj = json.loads(response.content.decode('utf-8'))
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
            ("main.smoke.TestFailedSmokeTests.test_assertTrueWoMsg "
             "failed: False is not true"),
            response_obj['failed_tests'])
        self.assertIn(
            "main.smoke.TestFailedSmokeTests.test_assertEqualWMsg failed: %s" %
            TestFailedSmokeTests.CUSTOM_TEST_MSG,
            response_obj['failed_tests'])

    def test_error(self):
        " Tests the error case (when we got exception during the smoke test). "
        test = self.TestWithException()
        (_, _, failed, errored, _, e_tests) = test.run()
        self.assertEqual(1, failed)
        self.assertEqual(1, errored)
        self.assertEqual(errored, len(e_tests))
        self.assertIn(
            "TestWithException.test_with_exception errored: %s" %
            BasicTest._EXC_MSG,
            e_tests[0])
        self.assertNotIn(BasicTest._FAIL_MSG, e_tests[0])

    def test_logging(self):
        """ On failure and on errors, messages should be logged by setup method.
        """
        _logged_msgs = []

        def logger_mock(msg):
            " Mocking the logger method for testing. "
            _logged_msgs.append(msg)

        class TestForLogging(self.TestWithException):
            " Mocked smoke test sub-class. "
            def __init__(self):
                " Set up mocked logger to this SmokeTest instance. "
                super(TestForLogging, self).__init__(logger_mock)

        TestForLogging().run()

        # After this, both fail and error message should be logged
        # (should be in _logged_msgs array).
        self.assertEqual(2, len(_logged_msgs))
        # As stated in TestWithException, the fake test will be the first for
        # sure.
        self.assertIn(BasicTest._FAIL_MSG, _logged_msgs[0])
        self.assertIn(
            "TestForLogging.test_with_exception errored: %s" %
            BasicTest._EXC_MSG,
            _logged_msgs[1])
