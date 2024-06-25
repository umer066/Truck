from django.urls import path
from .views import LocationListCreateAPIView, TruckTypeListCreateAPIView, BookingListCreateAPIView, BookingDetailUpdateDeleteAPIView

urlpatterns = [
    path('locations/', LocationListCreateAPIView.as_view(), name='location-list-create'),
    path('truck-types/', TruckTypeListCreateAPIView.as_view(), name='truck-type-list-create'),
    path('bookings/', BookingListCreateAPIView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailUpdateDeleteAPIView.as_view(), name='booking-detail-update-delete'),
]
