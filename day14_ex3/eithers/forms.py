from cProfile import label
from dataclasses import field
from django import forms
from .models import Question, Comment


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'
        
        labels = {
            'title' : 'Title',
            'issue_a' : 'RED TEAM',
            'issue_b' : 'BLUE TEAM',
        }


class CommentForm(forms.ModelForm):

    TEAM_A = '0'
    TEAM_B = '1'
    TEAM_CHOICES = [
        (TEAM_A, 'RED TEAM'),
        (TEAM_B, 'BLUE TEAM'),
    ]
    pick = forms.ChoiceField(choices=TEAM_CHOICES)


    class Meta:

        model = Comment
        exclude = ('question',)