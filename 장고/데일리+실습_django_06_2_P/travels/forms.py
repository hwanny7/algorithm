from dataclasses import field
from logging import PlaceHolder
from turtle import textinput
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    location = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'ex) 제주도'}))
    plan = forms.CharField(widget= forms.Textarea(attrs={'placeholder':'ex)슉.슈슉.'}))
    start_date = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'ex)2022-02-22'}))
    end_date = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'ex)2022-02-22'}))

    class Meta:
        model = Article
        fields = '__all__'