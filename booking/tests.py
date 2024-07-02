from django.test import TestCase
from .models import Room, Booking
from django.contrib.auth.models import User

class BookingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.room = Room.objects.create(name='Room1', price_per_night=100, number_of_beds=2)

    def test_create_booking(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/bookings/', {
            'room': self.room.id,
            'start_date': '2024-07-01',
            'end_date': '2024-07-05'
        })
        self.assertEqual(response.status_code, 201)
