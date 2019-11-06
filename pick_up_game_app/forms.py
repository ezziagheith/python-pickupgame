from django import forms
from .models import Event, Player

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'date', 'time', 'location', 'game_type')


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('user', 'age', 'gender', 'experience', 'pref_position')
