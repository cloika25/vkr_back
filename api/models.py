from django.db import models

class RegistrationField(models.Model):
    NameField = models.CharField(max_length=50)
    TypeField = models.CharField(max_length=30)

class RegistrationsModal(models.Model):
    NameOfRegistation = models.CharField(max_length=200, default='default')
    Fields = models.CharField(max_length=500)
    EventId = models.ForeignKey('Event', on_delete=models.CASCADE, default=-1)

class Event(models.Model):
    FullName = models.CharField(max_length=50)
    DateStart = models.DateTimeField(default=None)
    DateClose = models.DateTimeField(blank=True, null=True)
    AuthorUserId = models.BigIntegerField('User', default=None)
