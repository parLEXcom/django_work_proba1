from django.urls import path

from .views import Station_load

urlpatterns = [
        path('station', Station_load.as_view(), name="station"),
]