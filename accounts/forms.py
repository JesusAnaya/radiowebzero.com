from django import forms
from .models import Hour
from .widgets import TimeWidget

class HourForm(forms.ModelForm):
    time = forms.TimeField(widget=TimeWidget)

    class Meta:
        model = Hour
