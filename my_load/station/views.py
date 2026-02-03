from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from station.forms import StationNanber
from station.models import Station_namber


class Station_load(CreateView):
    form_class = StationNanber
    template_name = "station.html"
    success_url = reverse_lazy('home')

    def create_object(request):
        if request.method == "POST":
            form = StationNanber(request.POST)
            if form.is_valid():
                form.save()                      # Сохранение в базу [1]
        else:
            form_class = StationNanber

class Station_view(ListView):
    model = Station_namber
    template_name = "station_view.html"

    # def get_queryset(self):
    #     return Station_namber.objects.filter(title="Станция 1")


