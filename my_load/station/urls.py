from django.urls import path

from .views import Station_load, Station_view

urlpatterns = [
        path('station', Station_load.as_view(), name="station"),
        path('station_view', Station_view.as_view(), name="station_view"),

]