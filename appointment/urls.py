from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^book/$', views.book_appointment, name='book_appointment'),
    url(r'^book/detail/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
    url(r'^book/success/$', views.booking_success, name='booking_success'),
    url(r'^bookings/$', views.bookings, name='bookings'),
]