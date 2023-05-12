from django.contrib import admin
from .models import Flight_details
# Register your models here.
class FlightDetailsAdmin(admin.ModelAdmin):
    list_display = ['Fname','Fdate','Fstart','Fend']

admin.site.register(Flight_details,FlightDetailsAdmin)

