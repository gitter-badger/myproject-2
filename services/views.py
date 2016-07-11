from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.conf import settings

from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail

from .models import Service
from .forms import ContactForm


# Create your views here.
def home(request):
    services = Service.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    context = {
        'services': services,
    }
    return render(request, 'home/home.html', context)


def about(request):
    services = Service.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    form_class = ContactForm

    context = {
        'services': services,
        'form': form_class,
    }
    return render(request, 'home/about.html', context)


def contact(request):
    services = Service.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    form_class = ContactForm
    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('home/contact_template.txt')

            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['sbshrey@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            # send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'],
            # fail_silently=False)

            # send_mail('Test mail', 'this is working', settings.EMAIL_HOST_USER, ['sbshrey@gmail.com'],
            #           fail_silently=False)

            send_mail('New Appointment form submission', content, settings.EMAIL_HOST_USER, ['bahetishrey@gmail.com'],
                      fail_silently=False)

            messages.success(request, 'Contact is saved and further info will be email to you.')
            return redirect('contact')

    context = {
        'form': form_class,
        'services': services,
    }
    return render(request, 'home/contact.html', context)


def service_list(request):
    services = Service.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {
        'services': services,
    }
    return render(request, 'services/list.html', context)


def service_detail(request, id):
    services = Service.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    service = get_object_or_404(Service, id=id)
    context = {
        'service': service,
        'services': services,
    }
    return render(request, 'services/detail.html', context)


def get_services():
    services = Service.objects.values_list('service_name', flat=True)
    return [(services[i], services[i]) for i in range(len(services))]


def profile(request):
    return render(request, 'profile.html', {})
