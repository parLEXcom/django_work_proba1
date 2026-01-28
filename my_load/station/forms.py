from django import forms

from station.models import  Station_namber





class StationNanber(forms.ModelForm):
    class Meta:
        model = Station_namber
        fields = ['title', 'data', 'namber_1', 'namber_2', 'namber_3', 'namber_4', 'namber_5']
        data = forms.DateField(
            input_formats=['%d.%m.%Y', '%d/%m/%Y'],
            widget=forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'})      # Для HTML5 календаря
        )



