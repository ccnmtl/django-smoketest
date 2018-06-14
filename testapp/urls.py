try:
    from django.conf.urls import include, url
except ImportError:
    from django.conf.urls.defaults import include, url

from .views import TestView

urlpatterns = [
    url('^smoketest/$', include('smoketest.urls')),
    url('^extendable/$', TestView.as_view()),
]
