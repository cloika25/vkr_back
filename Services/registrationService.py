from api.models import *
from .util import isCreator
from Serializers.RegistrationModels import ListParticipants
import datetime


def userRegistratedOnEvent(stageId, userId):
    result = RegistrationsModal.objects.filter(UserId=userId, StageId=stageId).count()
    return result


def registerUser(data, user):
    stageId = data['StageId']
    eventId = data['EventId']
    if (not userRegistratedOnEvent(userId=user.id, stageId=stageId)):
        event = Event.objects.get(id=eventId)
        stage = Stage.objects.get(id=stageId)
        tempFields = data['Fields']
        registerRow = RegistrationsModal.objects.create(UserId_id=user.id, EventId_id=event.id, StageId_id=stage.id,
                                                        Fields=tempFields)
        registerRow.save()
        return "Вы успешно зарегистрированы", 200
    else:
        return "Вы уже зарегистрированы на данный этап", 400


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
    if isCreator(eventId, userId):
        allParticipants = RegistrationsModal.objects.filter(EventId=eventId)
        serializedData = ListParticipants(allParticipants, many=True).data
        prepData = parseRegistrations(serializedData)
        return prepData, 200
    else:
        return "Нет прав доступа", 400


def getAnalytics(eventId, userId):
    if isCreator(eventId, userId):
        allRows = list(
            RegistrationsModal.objects.filter(EventId=eventId).values('UserId__genderId', 'UserId__birth_date'))
        allCount = len(allRows)
        manCount = 0
        ages = {}
        for row in allRows:
            if row['UserId__genderId'] == 1:
                manCount += 1
            age = datetime.date.today().year - row['UserId__birth_date'].year
            if age in ages:
                ages[age] += 1
            else:
                ages[age] = 1
        womanCount = allCount - manCount
        responseBody = {
            "counts": {
                "all": allCount,
                "man": manCount,
                "woman": womanCount,
            },
            "ages": ages
        }
        return responseBody, 200
    else:
        return "Нет прав доступа", 400
