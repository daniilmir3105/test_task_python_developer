from rest_framework import viewsets
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        price = self.request.query_params.get('price')
        beds = self.request.query_params.get('beds')
        if price:
            queryset = queryset.filter(price_per_night=price)
        if beds:
            queryset = queryset.filter(number_of_beds=beds)
        return queryset

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
