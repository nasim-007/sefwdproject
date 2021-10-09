from django import forms
from .models import Carousel

class AddForm(forms.ModelForm):
    
    class Meta:
        model = Carousel
        fields = ('title', 'short_description', 'image')
