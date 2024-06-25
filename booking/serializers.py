from rest_framework import serializers
from .models import Location, TruckType, Booking

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class TruckTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckType
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
