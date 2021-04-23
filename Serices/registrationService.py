from api.models import *
from rest_framework.response import Response
from .util import fillResponse
from Serializers.RegistrationModels import ListParticipants


def userRegistratedOnEvent(eventId, userId):
    result = RegistrationsModal.objects.filter(UserId=userId, EventId=eventId).count()
    return result


def registerUser(data, user):
    response = Response()
    try:
        stageId = data['StageId']
        eventId = data['EventId']
        if (not userRegistratedOnEvent(userId=user.id, eventId=eventId)):
            event = Event.objects.get(id=eventId)
            stage = Stage.objects.get(id=stageId)
            tempFields = data['Fields']
            registerRow = RegistrationsModal.objects.create(UserId_id=user.id, EventId_id=event.id, StageId_id=stage.id,
                                                            Fields=tempFields)
            registerRow.save()
            response = fillResponse(response, "Вы успешно зарегистрированы", 200)
        else:
            response = fillResponse(response, "Вы уже зарегистрированы на данный этап", 400)
    except:
        response = fillResponse(response, "Произошла ошибка при регистрации", 400)
    return response


def parseRegistrations(items):
    result = []
    for item in items:
        tempData = {
            "id": item['id'],
            "StageName": item['StageId']['StageName'],
            "Fields": item['Fields'],
            "EventName": item['EventId']['FullName'],
        }
        result.append(tempData)
    return result


def getParticipants(eventId, userId):
    response = Response()
    try:
        allParticipants = RegistrationsModal.objects.filter(EventId=eventId)
        serializedData = ListParticipants(allParticipants, many=True).data
        prepData = parseRegistrations(serializedData)
        response = fillResponse(response, prepData, 200)
    except:
        response = fillResponse(response, "Ошибка получения регистраций", 400)
    return response
