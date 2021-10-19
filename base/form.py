from django import forms
from .models import Room

class RoomCreationForm(forms.ModelForm):
    class Meta:
        model= Room
        fields= '__all__'