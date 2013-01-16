class SmokeTest(object):
    def __init__(self):
        self._status = "PASS"

    def failed(self):
        return self._status == "FAIL"

    def passed(self):
        return self._status == "PASS"

    def reset(self):
        self._status = "PASS"

    def run(self):
        run, failed, passed, errored = 0, 0, 0, 0
        failed_tests = []
        errored_tests = []
        for d in dir(self):
            if d.startswith("test_"):
                run += 1
                try:
                    if hasattr(self, 'setUp'):
                        self.setUp()
                    getattr(self, d)()
                    if self.failed():
                        failed += 1
                        failed_tests.append(
                            self.__class__.__module__ + "."
                            + self.__class__.__name__ + "." + d)
                        self.reset()
                    else:
                        passed += 1
                    if hasattr(self, 'tearDown'):
                        self.tearDown()
                except:
                    errored += 1
                    errored_tests.append(
                        self.__class__.__module__ + "."
                        + self.__class__.__name__ + "." + d)
        return run, passed, failed, errored, failed_tests, errored_tests

    def assertEqual(self, a, b):
        if a != b:
            self._status = "FAIL"

    def assertNotEqual(self, a, b):
        if a == b:
            self._status = "FAIL"

    def assertTrue(self, t):
        if not t:
            self._status = "FAIL"

    def assertFalse(self, x):
        if x:
            self._status = "FAIL"

    def assertIs(self, a, b):
        if not a is b:
            self._status = "FAIL"

    def assertIsNot(self, a, b):
        if a is b:
            self._status = "FAIL"

    def assertIsNone(self, x):
        if x is not None:
            self._status = "FAIL"

    def assertIsNotNone(self, x):
        if x is None:
            self._status = "FAIL"

    def assertIn(self, a, b):
        if a not in b:
            self._status = "FAIL"

    def assertNotIn(self, a, b):
        if a in b:
            self._status = "FAIL"

    def assertIsInstance(self, a, b):
        if not isinstance(a, b):
            self._status = "FAIL"

    def assertNotIsInstance(self, a, b):
        if isinstance(a, b):
            self._status = "FAIL"

"""
TODO:
assertRaises(exc, fun, *args, **kwds)	fun(*args, **kwds) raises exc
assertRaisesRegexp(exc, re, fun, *args, **kwds)	fun(*args, **kwds)
   raises exc and the message matches re	2.7
assertAlmostEqual(a, b)	round(a-b, 7) == 0
assertNotAlmostEqual(a, b)	round(a-b, 7) != 0
assertGreater(a, b)	a > b	2.7
assertGreaterEqual(a, b)	a >= b	2.7
assertLess(a, b)	a < b	2.7
assertLessEqual(a, b)	a <= b	2.7
assertRegexpMatches(s, re)	regex.search(s)	2.7
assertNotRegexpMatches(s, re)	not regex.search(s)	2.7
assertItemsEqual(a, b)	sorted(a) == sorted(b) and works with unhashable
  objs 2.7
assertDictContainsSubset(a, b)	all the key/value pairs in a exist in b	2.7
assertMultiLineEqual(a, b)	strings	2.7
assertSequenceEqual(a, b)	sequences	2.7
assertListEqual(a, b)	lists	2.7
assertTupleEqual(a, b)	tuples	2.7
assertSetEqual(a, b)	sets or frozensets	2.7
assertDictEqual(a, b)	dicts	2.7
"""


class ApplicationTestResultSet(object):
    """ keeps track of:
    - number of test classes
    - number of tests run
    - number of tests passed
    - number of tests that errored out
    - number of tests that failed
    - failed tests
    - errored tests
    """
    def __init__(self, num_test_classes=0, num_tests_run=0,
                 num_tests_passed=0, num_tests_errored=0,
                 num_tests_failed=0, failed=None,
                 errored=None):
        self.num_test_classes = num_test_classes
        self.num_tests_run = num_tests_run
        self.num_tests_passed = num_tests_passed
        self.num_tests_errored = num_tests_errored
        self.num_tests_failed = num_tests_failed
        if failed is None:
            self.failed = []
        else:
            self.failed = failed
        if errored is None:
            self.errored = []
        else:
            self.errored = errored

    def passed(self):
        return self.num_tests_passed == self.num_tests_run
