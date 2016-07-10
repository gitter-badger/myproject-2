import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

from .models import CarModel, CarMake


# Create your views here.
# def get_car_make():
#     car_make = CarMake.objects.values_list('make', flat=True)
#     return [(i, car_make[i]) for i in range(len(car_make))]
#
#

def car_make():
    queryset = CarMake.objects.values_list('make', flat=True)
    return [(queryset[i], queryset[i]) for i in range(len(queryset))]


def car_model():
    queryset = CarModel.objects.values_list('model', flat=True)
    return [(queryset[i], queryset[i]) for i in range(len(queryset))]

#
# def car_make():
#     queryset = CarMake.objects.values_list('make', flat=True)
#     return queryset
#
#
# def car_model():
#     queryset = CarModel.objects.values_list('model', flat=True)
#     return queryset


def get_car_model(request):
    query = request.GET['make']
    car_make = CarMake.objects.values_list('id', 'make')
    car_model = CarModel.objects.values_list('model')
    for row in car_make:
        i = 0
        if query == row[i + 1]:
            val = row[i]
            car_model = CarModel.objects.filter(make=val).values_list('model', flat=True)
            break

    car_model_list = list(car_model)
    json_data = json.dumps(car_model_list)

    response = HttpResponse(json_data, content_type='application/json')

    return response
