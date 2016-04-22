from __future__ import unicode_literals

try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from .views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='smoketest'),
]
