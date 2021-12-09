from django import forms
from FrisbeeApp.models import League

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ["name"]