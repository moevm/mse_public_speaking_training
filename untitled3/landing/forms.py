from django import forms
from .models import *

class PresentationForm(forms.ModelForm):

    class Meta:
        model=Presentation
        exclude=[""]

