from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
     path('contact/', views.contact, name='contact'),
     path('about/', views.about, name='about'),
     path('book/', views.book, name='book'),
     path('booking_list/', views.booking_list, name='booking_list'),
 ]