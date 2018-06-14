from smoketest import SmokeTest
from exceptionstest import EXC_MSG

# raise exception here so we can test what will happen when
# we got any exception from smoke.py file
raise Exception(EXC_MSG)


class TestSmokeTestWithExceptions(SmokeTest):
    def test_with_import_exception(self):
        pass
