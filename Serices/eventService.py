from Serializers.Events import *

def getAllEvents():
    result = Event.objects.all()
    resultSerial = EventSerializer(result, many= True)
    return resultSerial

def createEvent(name, dateStart, dateClose = ''):
    responce = {
        'data': '',
        'code': ''
    }
    try:
        newEvent = Event
        if dateClose == '':
            newEvent = Event.objects.create(FullName=name, DateStart=dateStart)
        else:
            newEvent = Event.objects.create(FullName=name, DateStart=dateStart, DateClose=dateClose)
        newEvent.save()
        responce['data'] = f"Мероприятие {name} успешно создано"
        responce['code'] = 200
    except Exception:
        responce['data'] = f"Произошла ошибка при создании мероприятия {name}"
        responce['code'] = 400
    return responce