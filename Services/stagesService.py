from datetime import datetime
from django.utils.timezone import make_aware
from Serializers.Stages import *
from .util import fillResponse
from rest_framework.response import Response
from api.models import Event


def getStages(eventId):
    response = Response()
    try:
        allStages = Stage.objects.filter(EventId=eventId)
        if (allStages.count()):
            serializedData = StageSerializer(allStages, many=True).data
            response = fillResponse(response, serializedData, 200)
        else:
            response = fillResponse(response, [], 200)
    except:
        response = fillResponse(response, "Не удалось получить этапы", 400)
    return response


def createStage(data):
    response = Response()
    try:
        event = Event.objects.get(id=data['EventId'])
        format = FormatStage.objects.get(id=data['FormatId'])
        dateStart = make_aware(datetime.strptime(data["DateStart"], '%Y-%m-%dT%H:%M:%S'))
        dateEnd = make_aware(datetime.strptime(data["DateEnd"], '%Y-%m-%dT%H:%M:%S'))
        newStage = Stage.objects.create(StageName=data["StageName"],
                                        Description=data["Description"],
                                        DateStart=dateStart,
                                        DateEnd=dateEnd,
                                        FormatId=format,
                                        EventId=event)
        newStage.save()
        response = fillResponse(response, "Этап успешно создан", 200)
    except Exception:
        print(Exception)
        response = fillResponse(response, "Произошла ошибка при создании этапа", 400)
    return response


def updateStage(data):
    response = Response()
    try:
        tmpStage = Stage.objects.get(id=data["StageId"])
        if (tmpStage):
            dateStart = make_aware(datetime.strptime(data["DateStart"], '%Y-%m-%dT%H:%M:%S'))
            dateEnd = make_aware(datetime.strptime(data["DateEnd"], '%Y-%m-%dT%H:%M:%S'))
            event = Event.objects.get(id=data['EventId'])
            format = FormatStage.objects.get(id=data['FormatId'])
            if (tmpStage.EventId == event):
                tmpStage.StageName = data["StageName"]
                tmpStage.Description = data["Description"]
                tmpStage.DateStart = dateStart
                tmpStage.DateEnd = dateEnd
                tmpStage.FormatId = format
                tmpStage.save()
                response = fillResponse(response, "Этап успешно обновлен", 200)
            else:
                response = fillResponse(response, "Этап не соответствет мероприятию", 400)
    except:
        response = fillResponse(response, "Произошла ошибка при обновлении этапа", 400)
    return response


def removeStage(eventId, stageId):
    response = Response()
    try:
        stage = Stage.objects.get(id=stageId)
        event = Event.objects.get(id=eventId)
        if (stage.EventId == event):
            stage.delete()
            response = fillResponse(response, "Этап успешно удален", 200)
        else:
            response = fillResponse(response, "Этап не соответствет мероприятию", 400)
    except:
        pass
    return response


def getFormats():
    response = Response()
    try:
        formats = FormatStage.objects.all()
        formatsSer = FormatStagesSerializer(formats, many=True).data
        response = fillResponse(response, formatsSer, 200)
    except:
        response = fillResponse(response, "Произошла ошибка при получении форматов этапов", 400)
    return response


def getFields(stageId):
    response = Response()
    pass


def addFields(stageId, fields):
    pass


def updateFields(stageId, fields):
    """
    Обновление дополнительных полей регистрации на этап
    :param stageId:
    :param fields:
    :return:
    """
    stage = Stage.objects.get(id=stageId)
    stage.Fields = fields
    stage.save()
    return "Дополнительные поля успешно обновлены", 200
