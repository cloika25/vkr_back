from django.urls import path
from . import views
from rest_framework import routers

urlpatterns=[
    path('allUsers', views.allUsers),
    path('events', views.all_events),
    path('login', views.login),
    path('create_event', views.create_event),
    path('registration', views.registration),
]