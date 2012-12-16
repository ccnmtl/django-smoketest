
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
