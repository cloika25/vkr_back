from Serializers.Events import *
from Serializers.Users import ShortProfileSerialiser
from api.models import Profile
from rest_framework.response import Response
from back import settings
from .util import fillResponse


def getAllEvents():
    response = Response()
    try:
        events = Event.objects.all()
        eventsSerial = ShortEventSerializer(events, many=True).data
        for event in eventsSerial:
            tempProfile = Profile.objects.get(user_id=event["AuthorUserId"])
            if (tempProfile):
                tempProfile = ShortProfileSerialiser(tempProfile)
                tempProfile = tempProfile.data
                event['author'] = {
                    "firstName": tempProfile["user"]["first_name"],
                    "lastName": tempProfile["user"]["last_name"],
                    "photo": tempProfile["photo"]
                }
        response = fillResponse(response, eventsSerial, 200)
        return response
    except:
        response = fillResponse(response, "Произошла ошибка при получении мероприятий", 400)
        return response


def getUserEvents(user):
    result = Event.objects.filter(AuthorUserId=user.id)
    resultSerial = EventSerializer(result, many=True)
    return resultSerial.data


def getEvent(id):
    response = Response()
    try:
        event = Event.objects.filter(id=id)
        if (event.count()):
            eventSer = EventSerializer(event, many=True)
            response = fillResponse(response, eventSer.data, 200)
        else:
            response = fillResponse(response, 'Мероприятие не найдено', 404)
    except Exception:
        response = fillResponse(response, "Произошла ошибка при получении мероприятия", 400)
    return response


def getEventForEdit(id, userId):
    response = Response()
    try:
        event = Event.objects.filter(id=id)
        if (event.count()):
            if (event[0].AuthorUserId == userId):
                eventSer = EventSerializer(event, many=True)
                response = fillResponse(response, eventSer.data, 200)
            else:
                response = fillResponse(response, "Нет прав доступа", 401)
        else:
            response = fillResponse(response, 'Мероприятие не найдено', 404)
    except Exception:
        response = fillResponse(response, "Произошла ошибка при получении мероприятия", 400)
    return response


def createEvent(user, name, dateStart, dateClose=''):
    response = Response()
    try:
        if dateClose == '':
            newEvent = Event.objects.create(AuthorUserId=user.id, FullName=name, DateStart=dateStart)
        else:
            newEvent = Event.objects.create(AuthorUserId=user.id, FullName=name, DateStart=dateStart,
                                            DateClose=dateClose)
        newEvent.save()
        response = fillResponse(response, f"Мероприятие {name} успешно создано", 200)
    except Exception:
        response = fillResponse(response, f"Произошла ошибка при создании мероприятия {name}", 400)
    return response


def updateEvent(data):
    event = Event.objects.get(id=data['Id'])
    response = Response()
    if event:
        try:
            event.FullName = data['FullName']
            event.DateStart = data["DateStart"]
            event.DateClose = data["DateClose"]
            if (event.PhotoPreview is not None):
                if (data['PhotoPreview'] != 'null'):
                    event.PhotoPreview = data['PhotoPreview']
            else:
                if (settings.MEDIA_URL + event.PhotoPreview.name != data['PhotoPreview'] and data['PhotoPreview'] != 'null'):
                    event.PhotoPreview = data['PhotoPreview']
            if (event.PhotoMain is not None):
                if (data['PhotoMain'] != 'null'):
                    event.PhotoMain = data['PhotoMain']
            else:
                if (settings.MEDIA_URL + event.PhotoMain.name != data['PhotoMain'] and data['PhotoMain'] != 'null'):
                    event.PhotoMain = data['PhotoMain']
            event.Description = data['Description']
            event.save()
            response = fillResponse(response, "Мероприятие успешно обновлено", 200)
        except Exception:
            response = fillResponse(response, "Произошла ошибка при обновлении мероприятия", 400)
    else:
        response = fillResponse(response, "Мероприятие не найдено", 404)
    return response


def removeEvent(id):
    response = Response()
    try:
        tempEvent = Event.objects.filter(id=id)
        name = tempEvent[0].FullName
        tempEvent.delete()
        response = fillResponse(response, f'{name} успешно удалено', 200)
    except Exception:
        response = fillResponse(response, "Произошла ошибка при удалении мероприятия", 400)
    return response


def checkAuthor(eventId, userId):
    try:
        event = Event.objects.get(id=eventId)
        return event.AuthorUserId_id == userId
    except:
        return False