from django import forms
from first_app import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"

class AlbumForm(forms.ModelForm):

    class Meta:
        model = models.Album
        fields = "__all__"
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }
       