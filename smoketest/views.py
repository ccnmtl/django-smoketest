from django.http import HttpResponse
from django.conf import settings
import inspect
import importlib
from smoketest import SmokeTest


class ApplicationTestResultSet(object):
    """ keeps track of:
    - number of test classes
    - number of tests run
    - number of tests passed
    - number of tests that errored out
    - number of tests that failed
    """
    def __init__(self, num_test_classes=0, num_tests_run=0,
                 num_tests_passed=0, num_tests_errored=0,
                 num_tests_failed=0):
        self.num_test_classes = num_test_classes
        self.num_tests_run = num_tests_run
        self.num_tests_passed = num_tests_passed
        self.num_tests_errored = num_tests_errored
        self.num_tests_failed = num_tests_failed

    def passed(self):
        return self.num_tests_passed == self.num_tests_run


def test_class(cls):
    run, failed, passed, errored = 0, 0, 0, 0
    o = cls()
    if hasattr(o, 'setUp'):
        o.setUp()
    for d in dir(o):
        if d.startswith("test_"):
            run += 1
            try:
                getattr(o, d)()
                if o.failed():
                    print "failed one!"
                    failed += 1
                else:
                    passed += 1
            except:
                errored += 1
    if hasattr(o, 'tearDown'):
        o.tearDown()
    return run, passed, failed, errored


def test_application(app):
    """ should return an ApplicationTestResultSet """
    num_test_classes = 0
    num_tests_run = 0
    num_tests_passed = 0
    num_tests_failed = 0
    num_tests_errored = 0

    try:
        a = importlib.import_module("%s.smoke" % app)
        print "successfully imported smoke module for %s" % app
        for name, obj in inspect.getmembers(a, inspect.isclass):
            if not issubclass(obj, SmokeTest):
                continue
            if name == "SmokeTest":
                # skip the parent class, which is usually imported
                continue
            print name
            num_test_classes += 1
            run, passed, failed, errored = test_class(obj)
            num_tests_run += run
            num_tests_passed += passed
            num_tests_failed += failed
            num_tests_errored += errored

    except ImportError:
        # no 'smokes' module for the app
        pass
    except Exception, e:
        # anything else, probably an error in setUp()
        # or tearDown()
        num_tests_errored += 1
    return ApplicationTestResultSet(
        num_test_classes, num_tests_run,
        num_tests_passed, num_tests_errored,
        num_tests_failed)

def index(request):
    result_sets = [test_application(app) for app in settings.INSTALLED_APPS]
    all_passed = reduce(lambda x, y: x & y, [r.passed() for r in result_sets])
    num_test_classes = sum([r.num_test_classes for r in result_sets])
    num_tests_run = sum([r.num_tests_run for r in result_sets])
    num_tests_passed = sum([r.num_tests_passed for r in result_sets])
    num_tests_failed = sum([r.num_tests_failed for r in result_sets])
    num_tests_errored = sum([r.num_tests_errored for r in result_sets])
    if all_passed:
        status = "PASS"
    else:
        status = "FAIL"
    return HttpResponse(
        """%s
test classes: %d
tests run: %d
tests passed: %d
tests failed: %d
tests errored: %d""" % (status, num_test_classes, num_tests_run, num_tests_passed,
                       num_tests_failed, num_tests_errored))
