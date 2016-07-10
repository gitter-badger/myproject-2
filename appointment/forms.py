from django import forms

from .models import Appointment

from datetimewidget.widgets import DateWidget
from cars.models import CarMake, CarModel


class AppointmentForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AppointmentForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['car_make'] = forms.ModelChoiceField(
    #         queryset=CarMake.objects.values_list('make', flat=True)
    #     )
    #     self.fields['car_model'] = forms.ModelChoiceField(
    #         queryset=CarModel.objects.values_list('model', flat=True)
    #     )

    class Meta:
        model = Appointment
        widgets = {
            # Use localization and bootstrap 3
            'pick_up_date': DateWidget(attrs={'id': "pick_up_date"}, usel10n=True, bootstrap_version=3)
        }
        exclude = {
            'customer',
            'booking_id',
            'booking_date',
            'status',
        }
