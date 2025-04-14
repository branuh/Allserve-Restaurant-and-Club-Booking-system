from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('book/room/<int:room_id>/', views.book_room, name='book_room'),
    path('book/meeting_room/<int:meeting_room_id>/', views.book_meeting_room, name='meeting_room'),
    path('book/facility/<int:facility_id>/', views.book_facility, name='facility'),
    path('book/catering/<int:catering_id>/', views.book_catering, name='catering'),
    path('book/club/<int:club_id>/', views.book_club, name='club'),
    path('booking_list/', views.booking_list, name='booking_list'),
]