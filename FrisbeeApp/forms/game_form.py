from django import forms
from FrisbeeApp.models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["windspeed"]

