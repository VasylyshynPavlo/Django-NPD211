from django import forms
from .models import Word, WordCollection

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'translation']
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter word'}),
            'translation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter translation'}),
        }

class WordCollectionForm(forms.ModelForm):
    class Meta:
        model = WordCollection
        fields = ['title', 'language', 'public']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'language': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter language'}),
            'public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
