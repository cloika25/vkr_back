from Serializers.Events import *

def getAllEvents():
    result = Event.objects.all()
    resultSerial = EventSerializer(result, many= True)
    return resultSerial.data

def createEvent(name, dateStart, dateClose = ''):
    responce = {}
    try:
        newEvent = Event
        if dateClose == '':
            newEvent = Event.objects.create(FullName=name, DateStart=dateStart)
        else:
            newEvent = Event.objects.create(FullName=name, DateStart=dateStart, DateClose=dateClose)
        newEvent.save()
        responce['data'] = f"Мероприятие {name} успешно создано"
        responce['status'] = 200
    except Exception:
        responce['data'] = f"Произошла ошибка при создании мероприятия {name}"
        responce['status'] = 400
    return responce

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