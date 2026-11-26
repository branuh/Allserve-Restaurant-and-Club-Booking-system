Hotel, Restaurant & Club Management System

A full-stack web application that brings hotel, restaurant, and club operations into one platform. Built with a Laravel REST API and a React frontend, backed by MySQL.

Dashboard screenshot

Features
Hotel module: [room management, bookings, check-in/check-out, guest records]
Restaurant module: [menu management, order taking, billing]
Club module: [memberships, events, entry/tab management]
Authentication and roles: [admin / staff access, login, validation]
Reports/Dashboard: [daily sales, occupancy, etc.]

Keep only what actually works. Delete any line that isn't true.

Tech Stack
Layer	Technology
Backend	PHP, Laravel (REST API)
Frontend	React, JavaScript, HTML, CSS
Database	MySQL
Tools	Git, GitHub, Postman
Screenshots
Dashboard	Bookings	Orders
screenshots/dashboard.png	screenshots/bookings.png	screenshots/orders.png
Getting Started
Prerequisites
PHP 8.1+ and Composer
Node.js 18+ and npm
MySQL
Backend setup
bash
git clone https://github.com/[your-username]/[repo-name].git
cd [repo-name]/backend
composer install
cp .env.example .env
php artisan key:generate

Create a MySQL database, then update the DB_ values in .env:

bash
php artisan migrate --seed
php artisan serve
Frontend setup
bash
cd ../frontend
npm install
npm start

The app runs at http://localhost:3000 and the API at http://127.0.0.1:8000.

API Overview
Method	Endpoint	Description
POST	/api/login	[Authenticate a user]
GET	/api/rooms	[List rooms]
POST	/api/bookings	[Create a booking]
GET	/api/orders	[List restaurant orders]

Replace with your real endpoints (check routes/api.php).

What I Learned
[Designing a relational database for multiple connected modules]
[Building and consuming REST APIs between Laravel and React]
[Handling authentication and role-based access]
Future Improvements
[Payment integration, e.g. M-Pesa]
[Automated tests]
[Deployment to a live server]
Author

Enock Kipkoech Computer Science student, St Paul's University [LinkedIn link] | kipkoechenock20@gmail.com
