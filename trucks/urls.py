from django.urls import path
from .views import TruckListCreateAPIView, TruckRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('trucks/', TruckListCreateAPIView.as_view(), name='truck-list-create'),
    path('trucks/<int:pk>/', TruckRetrieveUpdateDestroyAPIView.as_view(), name='truck-detail'),
]
