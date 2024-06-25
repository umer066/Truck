from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Location, TruckType, Booking
from .serializers import LocationSerializer, TruckTypeSerializer, BookingSerializer

class LocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Location created successfully.'}, status=status.HTTP_201_CREATED, headers=headers)

    def handle_exception(self, exc):
        return Response({'error': str(exc)}, status=status.HTTP_400_BAD_REQUEST)

class TruckTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = TruckType.objects.all()
    serializer_class = TruckTypeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Truck type created successfully.'}, status=status.HTTP_201_CREATED, headers=headers)

    def handle_exception(self, exc):
        return Response({'error': str(exc)}, status=status.HTTP_400_BAD_REQUEST)

class BookingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Booking created successfully.'}, status=status.HTTP_201_CREATED, headers=headers)

    def handle_exception(self, exc):
        return Response({'error': str(exc)}, status=status.HTTP_400_BAD_REQUEST)

class BookingDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'Booking updated successfully.'}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Booking deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

    def handle_exception(self, exc):
        return Response({'error': str(exc)}, status=status.HTTP_400_BAD_REQUEST)
