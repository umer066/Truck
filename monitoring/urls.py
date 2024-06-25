from django.urls import path
from .views import MonitorStatusListCreateAPIView, MonitorStatusDetailAPIView

urlpatterns = [
    path('monitoring/', MonitorStatusListCreateAPIView.as_view(), name='monitor-status-list-create'),
    path('monitoring/<int:pk>/', MonitorStatusDetailAPIView.as_view(), name='monitor-status-detail'),
]
