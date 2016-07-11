from django.db import models

from django.utils import timezone
from django.core.urlresolvers import reverse

from services.views import get_services
from cars.views import car_make, car_model


# Create your models here.


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('auth.user', null=True)
    car_make = models.CharField(max_length=20, choices=car_make(), null=True)
    car_model = models.CharField(max_length=20, choices=car_model(), null=True)
    year_of_make = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=20, default='Gurgaon')
    pick_up_date = models.DateTimeField(default=timezone.now)
    service_type = models.CharField(max_length=20, choices=get_services(), null=True)
    additional_service = models.CharField(max_length=50, blank=True, null=True)
    booking_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('appointment:book_detail', args=(self.pk,))
