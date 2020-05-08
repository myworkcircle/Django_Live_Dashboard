from django import forms
from .models import Rooms, Hospital
from django.contrib.admin.widgets import AdminDateWidget

class calculation(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = [
            'icu',
            'endoscopy',
            'cardio',
            'neuro',
            'Doctor_rating',
            'vacancy',
        ]
    
class Hospital_Info(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'