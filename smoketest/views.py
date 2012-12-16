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


def test_class(cls):
    run, failed, passed, errored = 0, 0, 0, 0
    o = cls()
    failed_tests = []
    errored_tests = []
    if hasattr(o, 'setUp'):
        o.setUp()
    for d in dir(o):
        if d.startswith("test_"):
            run += 1
            try:
                getattr(o, d)()
                if o.failed():
                    print dir(o)
                    failed += 1
                    failed_tests.append(
                        o.__class__.__module__ + "."
                        + o.__class__.__name__ + "." + d)
                    o.reset()
                else:
                    passed += 1
            except:
                errored += 1
                errored_tests.append(
                    o.__class__.__module__ + "."
                    + o.__class__.__name__ + "." + d)
    if hasattr(o, 'tearDown'):
        o.tearDown()
    return run, passed, failed, errored, failed_tests, errored_tests


def test_application(app):
    """ should return an ApplicationTestResultSet """
    num_test_classes = 0
    num_tests_run = 0
    num_tests_passed = 0
    num_tests_failed = 0
    num_tests_errored = 0

    failed_tests = []
    errored_tests = []

    try:
        a = importlib.import_module("%s.smoke" % app)
        for name, obj in inspect.getmembers(a, inspect.isclass):
            if not issubclass(obj, SmokeTest):
                continue
            if name == "SmokeTest":
                # skip the parent class, which is usually imported
                continue
            num_test_classes += 1
            (run, passed, failed, errored,
             f_tests, e_tests) = test_class(obj)
            num_tests_run += run
            num_tests_passed += passed
            num_tests_failed += failed
            num_tests_errored += errored
            failed_tests = failed_tests + f_tests
            errored_tests = errored_tests + e_tests

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
        num_tests_failed, failed_tests,
        errored_tests)

def make_failed_report(result_sets):
    fails = []
    if sum([r.num_tests_failed for r in result_sets]) == 0:
        return ""
    for r in result_sets:
        if r.num_tests_failed > 0:
            for f in r.failed:
                fails.append(f)
    return "\n".join(["%s failed" % f for f in fails])

def make_errored_report(result_sets):
    errors = []
    if sum([r.num_tests_errored for r in result_sets]) == 0:
        return ""
    for r in result_sets:
        if r.num_tests_errored > 0:
            for f in r.errored:
                errors.append(f)
    return "\n".join(["%s errored" % e for e in errors])


def index(request):
    result_sets = [test_application(app) for app in settings.INSTALLED_APPS]
    all_passed = reduce(lambda x, y: x & y, [r.passed() for r in result_sets])
    num_test_classes = sum([r.num_test_classes for r in result_sets])
    num_tests_run = sum([r.num_tests_run for r in result_sets])
    num_tests_passed = sum([r.num_tests_passed for r in result_sets])
    num_tests_failed = sum([r.num_tests_failed for r in result_sets])
    num_tests_errored = sum([r.num_tests_errored for r in result_sets])
    failed_report = make_failed_report(result_sets)
    errored_report = make_errored_report(result_sets)
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
tests errored: %d
%s
%s""" % (status, num_test_classes, num_tests_run, num_tests_passed,
         num_tests_failed, num_tests_errored, failed_report,
         errored_report))
