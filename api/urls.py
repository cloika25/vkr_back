from django.urls import path
from . import views

urlpatterns = [
    path('allUsers', views.allUsers),
    # PersonalData
    path('cabinet', views.getPersonalData),
    path('editPersonalData', views.editPersonalData),
    path('getName', views.getName),
    # Events
    path('events', views.allEvents),
    path('my_events', views.myEvents),
    path('create_event', views.createEvent),
    path('update_event', views.updateEvent),
    path('remove_event', views.removeEvent),
    path('event', views.getEvent),
    path('eventForEdit', views.getEventForEdit),
    # Avatar
    path('avatar', views.getAvatar),
    path('updateAvatar', views.updateAvatar),
    path('removeAvatar', views.removeAvatar),
    # Stages
    path('stages', views.getStages),
    path('createStage', views.createStage),
    path('updateStage', views.updateStage),
    path('removeStage', views.removeStage),
    # AdditionalFields
    path('updateFields', views.updateFields),

    # Registrations
    path('registrationUser', views.registerUserToEvent),
    path('getMyRegistrations', views.getAllRegistrations),

    # Analytics
    path('getParticipants', views.getParticipants),
    path('getListParticipants', views.getListParticipants),
    path('getAnalytics', views.getAnalytics),

    # Utils
    path('getFormats', views.getFormats)
]
