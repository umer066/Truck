from rest_framework import generics, status
from rest_framework.response import Response
from .models import Compliance
from .serializers import ComplianceSerializer

class ComplianceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Compliance.objects.all()
    serializer_class = ComplianceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Compliance record created successfully.'}, status=status.HTTP_201_CREATED, headers=headers)

class ComplianceDetailUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compliance.objects.all()
    serializer_class = ComplianceSerializer
