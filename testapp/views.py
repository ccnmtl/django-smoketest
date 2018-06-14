"""
Just make sure that the main view is extendable
"""

from smoketest.views import IndexView


class TestView(IndexView):
    pass
