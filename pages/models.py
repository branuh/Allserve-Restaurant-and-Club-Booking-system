from django.db import models

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('room', 'Room Booking'),
        ('conference', 'Conference/Meeting Room'),
        ('meal', 'Meal Service'),
        ('recreation', 'Recreational Service'),
    ]
    SERVICE_TYPE_FIELDS = {
        'room': ['room_type', 'num_days'],
        'conference': ['conference_type', 'num_attendees', 'conference_date'],
        'meal': ['meal_type', 'meal_details'],
        'recreation': ['recreation_type', 'recreation_details'],
    }
    ROOM_CHOICES = [
        ('standard', 'Standard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
        ('executive', 'Executive'),
    ]
    CONFERENCE_CHOICES = [
        ('meeting', 'Meeting Room'),
        ('seminar', 'Seminar Room'),
        ('event', 'Event Hall'),
    ]
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('custom', 'Custom Meal'),
    ]
    RECREATION_CHOICES = [
        ('pool', 'Swimming Pool'),
        ('gym', 'Gym'),
        ('spa', 'Spa'),
        ('activities', 'Activities'),
    ]

    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES, blank=True, null=True)
    num_days = models.IntegerField(blank=True, null=True)
    conference_type = models.CharField(max_length=20, choices=CONFERENCE_CHOICES, blank=True, null=True)
    num_attendees = models.IntegerField(blank=True, null=True)
    conference_date = models.DateField(blank=True, null=True)
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES, blank=True, null=True)
    meal_details = models.TextField(blank=True, null=True)
    recreation_type = models.CharField(max_length=20, choices=RECREATION_CHOICES, blank=True, null=True)
    recreation_details = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.name} for {self.get_service_type_display()}"