
class SmokeTest(object):
    def __init__(self):
        self._status = "PASS"
        
    def assertTrue(self, t):
        if not t:
            print "bad assertTrue"
            self._status = "FAIL"

    def assertEquals(self, a, b):
        if a != b:
            self._status = "FAIL"

    def assertNotEquals(self, a, b):
        if a == b:
            self._status = "FAIL"
            
    def failed(self):
        return self._status == "FAIL"

    def passed(self):
        return self._status == "PASS"

    def reset(self):
        self._status = "PASS"
