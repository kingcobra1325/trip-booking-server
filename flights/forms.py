from django import forms
from .models import Flight

class MainForm(forms.ModelForm):
    AIRCRAFT_CHOICES = [
        ('Falcon 900', 'Falcon 900'),
        ('Falcon 600', 'Falcon 600'),
        ('AEM 700', 'AEM 700'),
        ('Boing 650', 'Boing 650'),
    ]
    
    ORIGIN_CHOICES = [
        ('Delhi Airport', 'Delhi Airport'),
        ('Mumbai Airport', 'Mumbai Airport'),
        ('Cochi Airport', 'Cochi Airport'),
        ('Banglore Airport', 'Banglore Airport'),
    ]
    
    DESTINATION_CHOICES = [
        ('London Airport', 'London Airport'),
        ('Dumbai Airport', 'Dumbai Airport'),
        ('Chenai Airport', 'Chenai Airport'),
        ('Kolkota Airport', 'Kolkota Airport'),
    ]

    aircraft = forms.ChoiceField(choices=AIRCRAFT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    origin = forms.ChoiceField(choices=ORIGIN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    destination = forms.ChoiceField(choices=DESTINATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    departure_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    departure_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    arrival_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    arrival_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    
    class Meta:
        model = Flight
        fields = ['aircraft', 'origin', 'destination', 'departure_date', 'departure_time', "arrival_date", 'flight_time']

# class MainForm(forms.Form):
#     aircraft_choices = [
#         ('Falcon 900', 'Falcon 900'),
#         ('Falcon 600', 'Falcon 600'),
#         ('AEM 700', 'AEM 700'),
#         ('Boing 650', 'Boing 650'),
#     ]
    
#     origin_choices = [
#         ('Delhi Airport', 'Delhi Airport'),
#         ('Mumbai Airport', 'Mumbai Airport'),
#         ('Cochi Airport', 'Cochi Airport'),
#         ('Banglore Airport', 'Banglore Airport'),
#     ]
    
#     destination_choices = [
#         ('London Airport', 'London Airport'),
#         ('Dumbai Airport', 'Dumbai Airport'),
#         ('Chenai Airport', 'Chenai Airport'),
#         ('Kolkota Airport', 'Kolkota Airport'),
#     ]
    
#     aircraft = forms.ChoiceField(choices=aircraft_choices, widget=forms.Select(attrs={'class': 'form-control'}))
#     origin = forms.ChoiceField(choices=origin_choices, widget=forms.Select(attrs={'class': 'form-control'}))
#     destination = forms.ChoiceField(choices=destination_choices, widget=forms.Select(attrs={'class': 'form-control'}))
#     departure_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
#     departure_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
#     arrival_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
#     arrival_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
#     flight_time = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '8 Hrs'}))
