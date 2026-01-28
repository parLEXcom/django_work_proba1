from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from station.forms import  StationNanber


class Station_load(CreateView):
    form_class = StationNanber
    template_name = "station.html"
    success_url = reverse_lazy('home')

    def create_object(request):
        if request.method == "POST":
            form = StationNanber(request.POST)
            if form.is_valid():
                form.save()  # Сохранение в базу [1]
                return reverse_lazy('home')
        else:
            form_class = StationNanber
