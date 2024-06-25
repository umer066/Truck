from django.urls import path
from .views import (
    DriverProfileListAPIView,
    DriverProfileCreateAPIView,
    DriverProfileRetrieveAPIView,
    DriverProfileUpdateAPIView,
    DriverProfileDestroyAPIView,
)

urlpatterns = [
    path('drivers/', DriverProfileListAPIView.as_view(), name='driver-list'),
    path('drivers/create/', DriverProfileCreateAPIView.as_view(), name='driver-create'),
    path('drivers/<int:pk>/', DriverProfileRetrieveAPIView.as_view(), name='driver-retrieve'),
    path('drivers/<int:pk>/update/', DriverProfileUpdateAPIView.as_view(), name='driver-update'),
    path('drivers/<int:pk>/delete/', DriverProfileDestroyAPIView.as_view(), name='driver-delete'),
]
