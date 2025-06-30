from django import forms
from .models import Tale

class TaleForm(forms.ModelForm):
    class Meta:
        model = Tale
        fields = ['titulo', 'contenido', 'imagen']
