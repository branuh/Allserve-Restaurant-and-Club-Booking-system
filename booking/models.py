from django.db import models
from django.contrib.auth.models import User

#create you models here
class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='rooms/', blank=True, null=True)

    def __str__(self):
        return self.name

class ConferenceRoom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='conferenceRoom/', blank=True, null=True)

    def __str__(self):
        return self.name

class RecreationalFacilities(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='recreation/', blank=True, null=True)

    def __str__(self):
        return self.name

class Catering(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='catering/', blank=True, null=True)

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=100,)
    description = models.TextField()
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='club/', blank=True, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rooms =models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    conference = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE, blank=True, null=True)
    facility = models.ForeignKey(RecreationalFacilities, on_delete=models.CASCADE, blank=True, null=True)
    catering = models.ForeignKey(Catering, on_delete=models.CASCADE, blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True)
    start_time = models.DateField()
    end_time = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking by {self.user.username} - {self.start_time}"