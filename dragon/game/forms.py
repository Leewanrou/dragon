from django import forms
from game.models import Game

class GameForm(forms.ModelForm):
    totalNum = forms.IntegerField()
    answerNum= forms.IntegerField()
    
    class Meta:
        model = Game
        fields = ['totalNum', 'answerNum']
    