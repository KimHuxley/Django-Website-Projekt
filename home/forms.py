from django import forms
from .models import Workout
from django.utils.timezone import now

from django import forms
from .models import Exercise

class WorkoutForm(forms.Form):
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all(), label="Ćwiczenie")
    sets = forms.IntegerField(min_value=1, max_value=10, label="Liczba serii")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Data")
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Godzina")
