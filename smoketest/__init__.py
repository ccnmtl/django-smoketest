
class SmokeTest(object):
    def __init__(self):
        self._status = "PASS"
            
    def failed(self):
        return self._status == "FAIL"

    def passed(self):
        return self._status == "PASS"

    def reset(self):
        self._status = "PASS"

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
assertRaisesRegexp(exc, re, fun, *args, **kwds)	fun(*args, **kwds) raises exc and the message matches re	2.7
assertAlmostEqual(a, b)	round(a-b, 7) == 0	 
assertNotAlmostEqual(a, b)	round(a-b, 7) != 0	 
assertGreater(a, b)	a > b	2.7
assertGreaterEqual(a, b)	a >= b	2.7
assertLess(a, b)	a < b	2.7
assertLessEqual(a, b)	a <= b	2.7
assertRegexpMatches(s, re)	regex.search(s)	2.7
assertNotRegexpMatches(s, re)	not regex.search(s)	2.7
assertItemsEqual(a, b)	sorted(a) == sorted(b) and works with unhashable objs	2.7
assertDictContainsSubset(a, b)	all the key/value pairs in a exist in b	2.7
assertMultiLineEqual(a, b)	strings	2.7
assertSequenceEqual(a, b)	sequences	2.7
assertListEqual(a, b)	lists	2.7
assertTupleEqual(a, b)	tuples	2.7
assertSetEqual(a, b)	sets or frozensets	2.7
assertDictEqual(a, b)	dicts	2.7
"""
