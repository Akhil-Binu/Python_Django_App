from django import forms

from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'Date'




class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        widgets  = {

            'booking_date' : DateInput(),

        }

        labels = {
            'p_name' : "Patients Name",
            'p_phone' : "Patients Phone Number",
            'p_email' : "Patients Email",
            'doc_name' : "Doctors Name"
        }
