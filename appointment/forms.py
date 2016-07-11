from django import forms
from django.forms import DateField

from django.conf import settings

from .models import Appointment

from datetimewidget.widgets import DateWidget


class AppointmentForm(forms.ModelForm):
    # pick_up_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Appointment
        widgets = {
            # Use localization and bootstrap 3
            'pick_up_date': DateWidget(attrs={'id': "pick_up_date"}, usel10n=True, bootstrap_version=3)
        }
        exclude = {
            'customer',
            'id',
            'booking_date',
            'status',
        }


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
