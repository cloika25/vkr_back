from django.urls import path
from . import views

urlpatterns = [
    path('allUsers', views.allUsers),
    # PersonalData
    path('editPersonalData', views.editPersonalData),
    path('profile', views.ProfileView.as_view()),
    # Events
    path('events', views.EventsViews.as_view()),
    path('event/<id>', views.EventView.as_view()),

    path('participants', views.ParticipantsView.as_view()),

    path('stages', views.StagesView.as_view()),

    path('myRegistrations', views.UserRegistrationsView.as_view()),

    path('my_events', views.myEvents),
    path('eventForEdit', views.getEventForEdit),
    # Avatar
    path('avatar', views.getAvatar),
    path('updateAvatar', views.updateAvatar),
    path('removeAvatar', views.removeAvatar),
    # Stages
    # path('stages', views.getStages),
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
