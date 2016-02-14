from smoketest import SmokeTest

"""
A testing framework is kind of a pain to properly test.

For now, this just tries to hit a few key parts of the actual
test running part. Ie, run through the various assert* methods
and make sure that setup/teardown are doing what they are
supposed to.
"""


class TestSmokeTest(SmokeTest):
    def setUp(self):
        self.been_setup = True
        self.been_toredown = False

    def tearDown(self):
        self.been_toredown = True
        self.been_setup = False

    def test_assertTrue(self):
        self.assertTrue(True)

    def test_assertEqual(self):
        self.assertEqual(13, 13)

    def test_setupteardown(self):
        self.assertTrue(self.been_setup)
        self.assertFalse(self.been_toredown)

    def test_assertNotEqual(self):
        self.assertNotEqual(10, 11)

    def test_assertIs(self):
        a = "foo"
        self.assertIs(a, "foo")

    def test_assertIsNot(self):
        a = "foo"
        self.assertIsNot(a, "bar")

    def test_assertIsNone(self):
        a = None
        self.assertIsNone(a)

    def test_assertIsNotNone(self):
        a = "foo"
        self.assertIsNotNone(a)

    def test_assertIn(self):
        a = [1, 2, 3, 4]
        b = 3
        self.assertIn(b, a)

    def test_assertNotIn(self):
        a = [1, 2, 3, 4]
        b = 5
        self.assertNotIn(b, a)

    def test_assertIsInstance(self):
        self.assertIsInstance(self, SmokeTest)

    def test_assertNotIsInstance(self):
        a = "foo"
        self.assertNotIsInstance(a, SmokeTest)

    def test_assertRaises(self):
        class FooError(BaseException):
            pass

        def f():
            raise FooError

        self.assertRaises(FooError, f)

    def test_assertAlmostEqual(self):
        a = 1.00000001
        b = 1.00000002
        self.assertAlmostEqual(a, b)

    def test_assertNotAlmostEqual(self):
        a = 1.000001
        b = 1.000002
        self.assertNotAlmostEqual(a, b)

    def test_assertGreater(self):
        self.assertGreater(1.5, 1.4)


class TestFailedSmokeTests(SmokeTest):
    CUSTOM_TEST_MSG = "Test failed as it should"

    def setUp(self):
        self.been_setup = True
        self.been_toredown = False

    def tearDown(self):
        self.been_toredown = True
        self.been_setup = False

    def test_assertTrueWoMsg(self):
        # test without message
        self.assertTrue(False)

    def test_assertEqualWMsg(self):
        # test with message
        self.assertEqual(13, 14, self.CUSTOM_TEST_MSG)
