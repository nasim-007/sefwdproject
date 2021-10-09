from django import forms
from .models import Corousel

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Corousel
        fields = ('title', 'short_description', 'image')