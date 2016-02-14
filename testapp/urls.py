try:
    from django.conf.urls import include, url
except ImportError:
    from django.conf.urls.defaults import include, url

urlpatterns = [
    url('^smoketest/$', include('smoketest.urls')),
]
