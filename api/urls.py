from django.urls import path
from . import views

urlpatterns=[
    path('allUsers', views.allUsers),
    path('events', views.all_events),
    path('my_events', views.my_events),
    path('cabinet', views.getPersonalData),
    path('avatar', views.getAvatar),
    path('updateAvatar', views.updateAvatar),
    path('removeAvatar', views.removeAvatar),
    path('editPersonalData', views.editPersonalData),
    path('getName', views.getName),
    path('create_event', views.create_event),
    path('remove_event', views.remove_event),
    path('update_event', views.update_event),
    path('event', views.get_event),
    path('eventForEdit', views.getEventForEdit),
]