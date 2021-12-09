from django import forms
from FrisbeeApp.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["first_name", "last_name", "jersey_number", "overall_rating", "height", "weight", "is_handle", "is_cutter"]



