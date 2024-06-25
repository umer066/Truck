from rest_framework import generics, status
from rest_framework.response import Response
from .models import Truck
from .serializers import TruckSerializer

class TruckListCreateAPIView(generics.ListCreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Truck created successfully.'}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class TruckRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Truck updated successfully.'}, status=status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Truck deleted successfully.'}, status=status.HTTP_200_OK)
