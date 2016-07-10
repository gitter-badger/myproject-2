# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_auto_20160709_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='car_make',
            field=models.CharField(choices=[('Ford', 'Ford'), ('Tata', 'Tata'), ('Hyundai', 'Hyundai')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='car_model',
            field=models.CharField(choices=[('Eco Sport', 'Eco Sport'), ('Figo', 'Figo'), ('Indica', 'Indica'), ('Indigo', 'Indigo'), ('Nano', 'Nano')], max_length=20, null=True),
        ),
    ]