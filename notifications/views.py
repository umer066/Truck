from rest_framework import generics, status
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Notification created successfully.'}, status=status.HTTP_201_CREATED, headers=headers)

class NotificationDetailAPIView(generics.RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
