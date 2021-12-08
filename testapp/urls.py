from django.urls import include, path

from .views import TestView

urlpatterns = [
    path('smoketest/', include('smoketest.urls')),
    path('extendable/', TestView.as_view()),
]
