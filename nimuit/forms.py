from django import forms
from .models import Appointment, Contact

class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ('name', 'email', 'department', 'time' )

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'department', 'message' )