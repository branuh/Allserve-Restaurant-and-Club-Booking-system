from django.shortcuts import render, redirect
from .forms import BookingForm
from .forms import Booking
# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def services(request):
    return render(request, 'pages/services.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'pages/book.html', {'form':form})

def booking_list(request):
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'pages/booking_list.html', {'bookings':bookings})