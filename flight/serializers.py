from rest_framework import serializers
from .models import Flight_details

class FlightDetailsSer(serializers.ModelSerializer):
    class Meta:
        model = Flight_details
        fields = "__all__"