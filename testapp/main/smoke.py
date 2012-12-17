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
