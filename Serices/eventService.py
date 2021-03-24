from Serializers.Events import *
from rest_framework.response import Response

def getAllEvents():
    result = Event.objects.all()
    resultSerial = EventSerializer(result, many=True)
    return resultSerial.data

def getUserEvents(user):
    result = Event.objects.filter(AuthorUserId=user.id)
    resultSerial = EventSerializer(result, many=True)
    return resultSerial.data

def getEvent(id):
    responce = {}
    try:
        event = Event.objects.filter(id= id)
        eventSer = EventSerializer(event, many= True)
        responce['data'] = eventSer.data
        responce['status'] = 200
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

def updateEvent(eventId, body):
    event = Event.objects.get(id = eventId)
    response = Response()
    if event:
        try:
            event.FullName = body["FullName"]
            event.DateStart = body["DateStart"]
            event.DateClose = body["DateClose"]
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