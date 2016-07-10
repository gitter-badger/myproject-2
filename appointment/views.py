# import json

from django.core.mail import send_mail
# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.contrib import messages
from django.utils import timezone

from .forms import AppointmentForm

from .models import Appointment
from services.models import Service


# Create your views here.

@login_required()
def bookings(request):
    appointments = Appointment.objects.filter(pick_up_date__gte=timezone.now()).order_by('-pick_up_date')
    context = {
        'appointments': appointments,
    }
    return render(request, 'appointment/bookings.html', context)


def booking_success(request):
    msg = "Your appointment is booked. To see details go to the given link"
    context = {
        'msg': msg,
    }
    return render(request, 'appointment/booking_success.html', context)


@login_required()
def book_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    context = {
        'appointment': appointment,
    }

    return render(request, 'appointment/book_detail.html', context)


@login_required()
def book_appointment(request):
    services = Service.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer = request.user
            messages.success(request, 'Appointment is saved')
            instance.save()
            send_mail('Test mail', 'this is working', settings.EMAIL_HOST_USER, ['bahetishrey@gmail.com'],
                      fail_silently=False)
            return redirect('appointment:booking_success')
        else:
            # x = form.errors.as_data()
            messages.error(request, 'Appointment is not saved')
    else:
        form = AppointmentForm()

    context = {
        'form': form,
        'services': services,
    }

    return render(request, 'appointment/book.html', context)
