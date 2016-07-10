from django.db import models

from django.utils import timezone
from django.core.urlresolvers import reverse

from django.utils.deconstruct import deconstructible

from services.views import get_services
from cars.views import car_make, car_model


# Create your models here.


@deconstructible
class Appointment(models.Model):
    customer = models.ForeignKey('auth.user', null=True)
    booking_id = models.IntegerField(null=True)
    car_make = models.CharField(max_length=20, choices=car_make(), null=True)
    car_model = models.CharField(max_length=20, choices=car_model(), null=True)
    year_of_make = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=20, default='Gurgaon')
    pick_up_date = models.DateField(default=timezone.now)
    service_type = models.IntegerField(choices=get_services(), null=True)
    additional_service = models.CharField(max_length=50, blank=True, null=True)
    booking_date = models.DateField(default=timezone.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('appointment:book_detail', args=(self.pk,))
