from django.contrib import admin

from .models import Appointment


# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'car_make',
        'car_model',
        'year_of_make',
        'location',
        'service_type',
        'additional_service',
        'booking_date',
        'pick_up_date',
        'status',
    )


admin.site.register(Appointment, AppointmentAdmin)
