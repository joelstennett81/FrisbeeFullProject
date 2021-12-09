from django import forms
from FrisbeeApp.models import PlayerGame

class PlayerGameForm(forms.ModelForm):
    class Meta:
        model = PlayerGame
        fields = ["goals", "assists", "turnovers", "completions", "throwaways", "drops", "passing_yards", "receiving_yards", "touches"]
