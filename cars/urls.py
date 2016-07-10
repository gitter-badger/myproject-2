from django.conf.urls import url

from .views import get_car_model

urlpatterns = [
    url(r'^model/$', get_car_model, name='get_car_model'),
]