from django.conf.urls.defaults import patterns, include

urlpatterns = patterns(
    '',
    ('^smoketest/$', include('smoketest.urls')),
)
