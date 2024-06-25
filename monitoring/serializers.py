from rest_framework import serializers
from .models import MonitorStatus

class MonitorStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorStatus
        fields = '__all__'
