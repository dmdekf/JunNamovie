from django import forms
from .models import Score


class ScoreForm(forms.ModelForm):
    score = forms.FloatField(required=False, max_value=10, min_value=0,
                             label="평가 점수", widget=forms.NumberInput(attrs={'placeholder': '10.0'}))

    class Meta:
        model = Score
        fields = ['score']
