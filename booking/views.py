from django.shortcuts import render,redirect,get_object_or_404
from .models import Room,ConferenceRoom,RecreationalFacilities,Catering,Club,Booking
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request, 'accounts/../templates/home.html')

def services(request):
    rooms = Room.objects.all()
    meeting_rooms = ConferenceRoom.objects.all()
    facilities = RecreationalFacilities.objects.all()
    catering = Catering.objects.all()
    club = Club.objects.all()
    return render(request, 'booking/services.html', {'rooms':rooms, 'conference':conference, 'facilities':facilities, 'catering':catering, 'club':club})

@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        notes = request.POST['notes']
        Booking.objects.create(user=request.user, room=room, start_time=start_time, end_time=end_time, notes=notes)
        return redirect('booking_list')
    return render(request, 'booking/book_room.html', {'room':room})

@login_required()
def book_meeting_room(request, meeting_room_id):
    meeting_room = get_object_or_404(ConferenceRoom, pk=meeting_room_id)
    if request.method == 'POST':
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        notes = request.POST['notes']
        Booking.objects.create(user=request, meeting_room=meeting_room, start_time=start_time, end_time=end_time, notes=notes)
        return redirect('booking_list')
    return render(request, 'booking/book_meeting_room.html', {'meeting_room':meeting_room})

@login_required()
def book_facility(request, facility_id):
    facility = get_object_or_404(RecreationalFacilities, pk=facility_id)
    if request.method == 'POST':
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        notes = request.POST['notes']
        Booking.objects.create(user=request, facility=facility, start_time=start_time, end_time=end_time, notes=notes)
        return redirect('booking_list')
    return render(request, 'booking/facility.html', {'facility':facility})

@login_required()
def book_catering(request, catering_id):
    catering = get_object_or_404(Catering, pk=catering_id)
    if request.method == 'POST':
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        notes = request.POST['notes']
        Booking.objects.create(user=request, catering=catering, start_time=start_time, end_time=end_time, notes=notes)
        return redirect('booking_list')
    return render(request, 'booking/catering.html', {'catering':catering})

@login_required()
def book_club(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    if request.method == 'POST':
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        notes = request.POST['notes']
        Booking.objects.create(user=request, club=club, start_time=start_time, end_time=end_time, notes=notes)
        return redirect('booking_list')
    return render(request, 'booking/club.html', {'club':club})

@login_required()
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'bookings':bookings})