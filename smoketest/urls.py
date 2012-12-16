from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    '',
    (r'^$', 'smoketest.views.index'),
)
