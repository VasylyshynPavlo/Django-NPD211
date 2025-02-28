from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'translation']
        widgets = {
            'word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть слово'}),
            'translation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть переклад'}),
        }
