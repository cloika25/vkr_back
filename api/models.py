from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from datetime import date


class RegistrationsModal(models.Model):
    UserId = models.ForeignKey('Profile', on_delete=models.CASCADE, default=None)
    StageId = models.ForeignKey('Stage', on_delete=models.CASCADE, default=None)
    Fields = JSONField(null=True)
    EventId = models.ForeignKey('Event', on_delete=models.CASCADE, default=-1)


class FormatStage(models.Model):
    name = models.CharField(max_length=100, default='', null=True)

    def __str__(self):
        return self.name


class Stage(models.Model):
    StageName = models.CharField(max_length=200, default='')
    Description = models.TextField(default=None, null=True)
    DateStart = models.DateTimeField(default=None, null=True)
    DateEnd = models.DateTimeField(default=None, null=True)
    FormatId = models.ForeignKey('FormatStage', on_delete=models.DO_NOTHING, default=0)
    EventId = models.ForeignKey('Event', on_delete=models.CASCADE, default=1)
    Fields = JSONField(null=True)

    def __str__(self):
        return self.StageName


class Event(models.Model):
    FullName = models.CharField(max_length=50)
    DateStart = models.DateTimeField(default=None)
    DateClose = models.DateTimeField(blank=True, null=True)
    AuthorUserId = models.ForeignKey('Profile', on_delete=models.DO_NOTHING)

    PhotoPreview = models.ImageField(upload_to="events/preview", null=True, blank=True)
    PhotoMain = models.ImageField(upload_to="events/main", null=True, blank=True)
    Description = models.TextField(default=None, null=True)

    def __str__(self):
        return self.FullName


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    genderId = models.IntegerField(default=None, null=True)
    birth_date = models.DateField(default="1990-01-01")
    photo = models.ImageField(upload_to="users", null=True)

    def getAge(self):
        return (date.today() - self.birth_date).year

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
