"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from services.views import home, about, contact
import allauth.account.views


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^admin/', admin.site.urls),
    url(r'^cars/', include('cars.urls', namespace='cars')),
    url(r'^services/', include('services.urls', namespace='services')),
    url(r'^appointment/', include('appointment.urls', namespace='appointment')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/login/$', allauth.account.views.login, name='login'),
    url(r'^accounts/logout/$', allauth.account.views.logout, name='logout'),
    url(r'^accounts/signup/$', allauth.account.views.signup, name='signup'),
]
