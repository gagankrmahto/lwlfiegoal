from cProfile import label
from django import forms

class AnswerForm(forms.Form):
    question = forms.CharField(label='ques', max_length=100)
    points = forms.IntegerField(label='points')
    language = forms.CharField(label='language')

