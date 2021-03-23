from django import forms
from .models import PersonType, Person, PlaceType, Place

class PersonForm(forms.ModelForm):
    class Meta:
        model= Person
        fields='__all__'

class PlaceForm(forms.ModelForm):
    class Meta:
        model= Place
        fields='__all__'
