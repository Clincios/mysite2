from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from .models import Contact
from .models import Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=255, label='Search')

    class Meta:
        fields = ['search_query']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('firstname','lastname','body')