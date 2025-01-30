from django.urls import path

from .views import IndexView

app_name = 'smoketest'

urlpatterns = [
    path('', IndexView.as_view(), name='smoketest'),
]
