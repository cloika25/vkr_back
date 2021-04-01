from Serializers.Events import *
from Serializers.Users import ShortProfileSerialiser
from api.models import Profile
from rest_framework.response import Response

from back import settings


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
                event['author'] ={
                    "firstName": tempProfile["user"]["first_name"],
                    "lastName": tempProfile["user"]["last_name"],
                    "photo": tempProfile["photo"]
                }
        response.data = eventsSerial
        response.status_code = 200
        return response
    except:
        response.data = "Произошла ошибка при получении мероприятий"
        response.status_code = 400

def getUserEvents(user):
    result = Event.objects.filter(AuthorUserId=user.id)
    resultSerial = EventSerializer(result, many=True)
    return resultSerial.data

def getEvent(id):
    responce = {}
    try:
        event = Event.objects.filter(id= id)
        if (event.count()):
            eventSer = EventSerializer(event, many= True)
            responce['data'] = eventSer.data
            responce['status'] = 200
        else:
            responce['data'] = 'Мероприятие не найдено'
            responce['status'] = 404
    except Exception:
        responce['data'] = f"Произошла ошибка при получении мероприятия"
        responce['status'] = 400
    return responce

def createEvent(user, name, dateStart, dateClose = ''):
    responce = {}
    try:
        if dateClose == '':
            newEvent = Event.objects.create(AuthorUserId=user.id, FullName=name, DateStart=dateStart)
        else:
            newEvent = Event.objects.create(AuthorUserId=user.id, FullName=name, DateStart=dateStart, DateClose=dateClose)
        newEvent.save()
        responce['data'] = f"Мероприятие {name} успешно создано"
        responce['status'] = 200
    except Exception:
        responce['data'] = f"Произошла ошибка при создании мероприятия {name}"
        responce['status'] = 400
    return responce

def updateEvent(data):
    event = Event.objects.get(id = data['Id'])
    response = Response()
    if event:
        try:
            event.FullName = data['FullName']
            event.DateStart = data["DateStart"]
            event.DateClose = data["DateClose"]
            if (settings.MEDIA_URL + event.PhotoPreview.name != data['PhotoPreview']):
                event.PhotoPreview = data['PhotoPreview']
            if (settings.MEDIA_URL + event.PhotoMain.name != data['PhotoMain']):
                event.PhotoMain = data['PhotoMain']
            event.Description = data['Description']
            event.save()
        except Exception:
            response.status_code = 400
            response.data = "Произошла ошибка при обновлении мероприятия"
    else:
        response.status_code = 404
        response.data = "Мероприятие не найдено"
    return response

def removeEvent(id):
    responce = {}
    try:
        tempEvent = Event.objects.filter(id = id)
        name = tempEvent[0].FullName
        tempEvent.delete()
        responce['data'] = f'{name} успешно удалено'
        responce['status'] = 200
    except Exception:
        responce['status'] = 404
        responce['data'] = "Произошла ошибка при удалении мероприятия"
    return responce