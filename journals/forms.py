from django import forms
from .models import journal

class journalCreationForm(forms.ModelForm):
    class Meta:
        model = journal
        fields = ['topic', 'body', 'writer']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),
        }

