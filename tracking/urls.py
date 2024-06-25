from django.urls import path
from .views import TrackingListCreateAPIView, TrackingRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('tracking/', TrackingListCreateAPIView.as_view(), name='tracking-list-create'),
    path('tracking/<int:pk>/', TrackingRetrieveUpdateDestroyAPIView.as_view(), name='tracking-detail'),
]
