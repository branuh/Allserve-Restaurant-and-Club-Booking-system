# Generated by Django 5.1.7 on 2025-04-17 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('room', 'Room Booking'), ('conference', 'Conference/Meeting Room'), ('meal', 'Meal Service'), ('recreation', 'Recreational Service')], max_length=20)),
                ('room_type', models.CharField(blank=True, choices=[('standard', 'Standard'), ('deluxe', 'Deluxe'), ('suite', 'Suite'), ('executive', 'Executive')], max_length=20, null=True)),
                ('num_days', models.IntegerField(blank=True, null=True)),
                ('conference_type', models.CharField(blank=True, choices=[('meeting', 'Meeting Room'), ('seminar', 'Seminar Room'), ('event', 'Event Hall')], max_length=20, null=True)),
                ('num_attendees', models.IntegerField(blank=True, null=True)),
                ('conference_date', models.DateField(blank=True, null=True)),
                ('meal_type', models.CharField(blank=True, choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('custom', 'Custom Meal')], max_length=20, null=True)),
                ('meal_details', models.TextField(blank=True, null=True)),
                ('recreation_type', models.CharField(blank=True, choices=[('pool', 'Swimming Pool'), ('gym', 'Gym'), ('spa', 'Spa'), ('activities', 'Activities')], max_length=20, null=True)),
                ('recreation_details', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
