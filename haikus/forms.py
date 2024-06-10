from django import forms
from .models import Haiku


class HaikuCreateForm(forms.ModelForm):
    class Meta:
        model = Haiku
        fields = ('poem', 'description', 'image',)