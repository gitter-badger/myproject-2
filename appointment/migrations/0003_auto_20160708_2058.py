# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20160708_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='booking_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='additional_service',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]