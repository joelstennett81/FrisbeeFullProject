from django import forms
from FrisbeeApp.models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ["city", "mascot", "overall_rating"]
