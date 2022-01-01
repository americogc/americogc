from django.contrib import admin

#importar el modelo
from core.models import Booking

# Register your models here.
#crear la clase admin
class BookingAdmin(admin.ModelAdmin):
    pass

#crear el registro admin
admin.site.register(Booking, BookingAdmin)
