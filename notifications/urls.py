from django.urls import path
from .views import NotificationListCreateAPIView, NotificationDetailAPIView

urlpatterns = [
    path('notifications/', NotificationListCreateAPIView.as_view(), name='notification-list-create'),
    path('notifications/<int:pk>/', NotificationDetailAPIView.as_view(), name='notification-detail'),
]
