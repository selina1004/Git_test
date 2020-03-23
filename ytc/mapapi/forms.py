from django import forms
from .models import Place_info

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Place_info
        fields = ('author', 'title', 'lat', 'lng', 'road_adr', 'num_adr', 'tel', 'created_date',)