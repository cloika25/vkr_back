from django.db import models
from django.contrib.auth.models import User
from datetime import date

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
    AuthorUserId = models.BigIntegerField(null=True)

    PhotoPreview = models.ImageField(upload_to="events", null=True)
    PhotoMain = models.ImageField(upload_to="events", null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    genderId = models.IntegerField(default=None, null=True)
    birth_date = models.DateField(default="1990-01-01")

    def getAge(self):
        return (date.today() - self.birth_date).year

