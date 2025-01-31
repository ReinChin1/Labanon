from django import forms
from .models import BlotterEntry

class BlotterEntryForm(forms.ModelForm):
    class Meta:
        model = BlotterEntry
        fields = ['name', 'address', 'date', 'contact_number']