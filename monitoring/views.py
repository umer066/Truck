from rest_framework import generics, status
from rest_framework.response import Response
from .models import MonitorStatus
from .serializers import MonitorStatusSerializer

class MonitorStatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = MonitorStatus.objects.all()
    serializer_class = MonitorStatusSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Monitor status created successfully.'}, status=status.HTTP_201_CREATED, headers=headers)

class MonitorStatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonitorStatus.objects.all()
    serializer_class = MonitorStatusSerializer
