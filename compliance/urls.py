from django.urls import path
from .views import ComplianceListCreateAPIView, ComplianceDetailUpdateAPIView

urlpatterns = [
    path('compliance/', ComplianceListCreateAPIView.as_view(), name='compliance-list-create'),
    path('compliance/<int:pk>/', ComplianceDetailUpdateAPIView.as_view(), name='compliance-detail-update'),
]
