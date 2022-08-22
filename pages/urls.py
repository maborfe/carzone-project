from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('cars', views.cars, name='cars'),
    path('search', views.search, name='search'),
    path('services', views.services, name='services'),
    path('car_details', views.car_details, name='car_details'),
]
