from .models import Article, Comment
from django import forms
from django.db import models

team = ( 
    (True, 'RED TEAM'),
    (False, 'BLUE TEAM'),
)

class CommentForm(forms.ModelForm):
    pick = forms.ChoiceField(widget = forms.Select(), choices = team)

    class Meta:
        model = Comment
        exclude = ('article',)

        
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
