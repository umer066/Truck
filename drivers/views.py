from rest_framework import generics, status
from rest_framework.response import Response
from .models import DriverProfile
from .serializers import DriverProfileSerializer

class DriverProfileListAPIView(generics.ListAPIView):
    queryset = DriverProfile.objects.all()
    serializer_class = DriverProfileSerializer

class DriverProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = DriverProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Driver profile created successfully.'}, status=status.HTTP_201_CREATED, headers=headers)

class DriverProfileRetrieveAPIView(generics.RetrieveAPIView):
    queryset = DriverProfile.objects.all()
    serializer_class = DriverProfileSerializer

class DriverProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = DriverProfile.objects.all()
    serializer_class = DriverProfileSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'Driver profile updated successfully.'}, status=status.HTTP_200_OK)

class DriverProfileDestroyAPIView(generics.DestroyAPIView):
    queryset = DriverProfile.objects.all()
    serializer_class = DriverProfileSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Driver profile deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
