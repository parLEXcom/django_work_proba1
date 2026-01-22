from django import forms

from station.models import  Station_namber





class StationNanber(forms.ModelForm):
    class Meta:
        model = Station_namber
        fields = ['title', 'data', 'namber_1', 'namber_2', 'namber_3', 'namber_4', 'namber_5']



