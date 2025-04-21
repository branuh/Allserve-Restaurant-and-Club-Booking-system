from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service_type', 'room_type', 'num_days', 'conference_type', 'num_attendees', 'conference_date', 'meal_type', 'meal_details', 'recreation_type', 'recreation_details', 'name', 'email', 'phone']
        widgets = {
            'conference_date': forms.DateInput(attrs={'type': 'date'}),
            'meal_details': forms.Textarea(attrs={'rows': 3}),
            'recreation_details': forms.Textarea(attrs={'rows': 3}),
        }