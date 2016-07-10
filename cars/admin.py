from django.contrib import admin

from .models import CarMake, CarModel


# Register your models here.
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'model')
    list_editable = ('model',)


admin.site.register(CarMake)
admin.site.register(CarModel, CarModelAdmin)
