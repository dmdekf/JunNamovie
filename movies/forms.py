from django import forms
from .models import Score


class ScoreForm(forms.ModelForm):
    score = forms.FloatField()

    class Meta:
        model = Score
        fields = ['score']
