from django import forms
from Stickynotes.models import Guest, Business, Booking


class GuestDetailForm(forms.ModelForm):
    BOOL_CHOICES = [(True, 'Yes'), (False, 'No')]
    is_business_guest = forms.BooleanField(
        widget=forms.RadioSelect(choices=BOOL_CHOICES),
        required=False
    )

    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'email', 'phone')


class BusinessDetailForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = ('name',)

class BookingDetailForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('room_type', 'date', 'number_of_nights')
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}



