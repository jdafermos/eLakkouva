from django import forms
from django.contrib.gis import forms
from .models import Pits, Bulbs, Leaks

class thePitsForm(forms.ModelForm):
    class Meta:
        model = Pits
        fields = ()

class theBulbsForm(forms.ModelForm):
    class Meta:
        model = Bulbs
        fields = ()

class theLeaksForm(forms.ModelForm):
    class Meta:
        model = Leaks
        fields = ()