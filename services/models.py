from django.core.urlresolvers import reverse
from django.utils import timezone

from django.db import models

import logging

logger = logging.getLogger(__name__)


# Create your models here.

class Service(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d',
                              blank=True,
                              null=True,
                              height_field="height_field",
                              width_field="width_field")

    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.service_name

    def get_absolute_url(self):
        return reverse('services:service_detail', kwargs={'id': self.id})
