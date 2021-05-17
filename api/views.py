import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import Services.authService as authService
import Services.eventService as eventService
import Services.registrationService as registrationService
import Services.stagesService as stageService
from Services.util import fillResponse

from models import Event
from Serializers import ShortEventSerializer


@api_view(['GET'])
def allUsers(request):
    response = authService.getAllUsers()
    return Response(response.data)


# PersonaData block
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPersonalData(request):
    """
    Получение личных данных пользователя

    :param request:
    :return:
    """
    response = authService.getPersonalData(request.user)
    return response


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def editPersonalData(request):
    """
    Редактирование персональных данных пользователя

    :param request:
    :return:
    """
    dataRequest = json.loads(request.read())
    body = dataRequest['body']
    response = Response()
    try:
        data, status = authService.editPersonalData(request.user, body)
        response = fillResponse(response, data, status)
    except BaseException:
        response = fillResponse(response, "Произшла внутренняя ошибка", 404)
    return response


@api_view(['POST'])
def getName(request):
    """
    Получить краткое описание пользователя (для шапки сайта)

    :param request:
    :return:
    """
    data = request.data['id']
    response = authService.getName(data)
    return response


# PersonalData block END

# CRUD EVENTS
@api_view(['GET'])
def allEvents(request):
    """
    Получить список всех мероприятий

    :param request:
    :return:
    """
    response = eventService.getAllEvents()
    return response

class EventViews(RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = ShortEventSerializer

@api_view(['GET'])
def myEvents(request):
    """
    Получить все мероприятия, которые создал пользователь

    :param request:
    :return:
    """
    response = eventService.getUserEvents(request.user)
    return Response(response)


@api_view(['POST'])
def createEvent(request):
    """
    Создание мероприятия

    :param request:
    :return:
    """
    data = json.loads(request.read())
    FullName = data['FullName']
    DateStart = data['DateStart']
    DateClose = data['DateClose']
    response = eventService.createEvent(request.user, FullName, DateStart, DateClose)
    return response


@api_view(['POST'])
def removeEvent(request):
    """
    Удаление мероприятия

    :param request:
    :return:
    """
    data = json.loads(request.read())
    id = data['id']
    response = eventService.removeEvent(id)
    return response


@api_view(['PUT'])
def updateEvent(request):
    """
    Обновление данных мероприятия

    :param request:
    :return:
    """
    data = request.data
    response = eventService.updateEvent(data)
    return response


@api_view(['POST'])
def getEvent(request):
    """
    Получить описание мероприятия

    :param request:
    :return:
    """
    data = json.loads(request.read())
    id = data['id']
    response = eventService.getEvent(id)
    return response


@api_view(['POST'])
def getEventForEdit(request):
    """
    Получить личные данные пользователя

    :param request:
    :return:
    """
    data = json.loads(request.read())
    id = data['id']
    userId = request.user.id
    response = eventService.getEventForEdit(id, userId)
    return response


# CRUD Events END


# CRUD AVATAR
@api_view(['GET'])
def getAvatar(request):
    """
    Получить аватар пользователя

    :param request:
    :return:
    """
    userId = request.user.id
    response = authService.getAvatar(userId)
    return response


@api_view(['POST'])
def updateAvatar(request):
    """
    Обновление аватарки пользователя

    :param request:
    :return:
    """
    photo = request.data['photo']
    userId = request.user.id
    response = authService.updateAvatar(photo, userId)
    return response


@api_view(['GET'])
def removeAvatar(request):
    """
    Удалить аватар пользователя

    :param request:
    :return:
    """
    userId = request.user.id
    response = authService.removeAvatar(userId)
    return response


# CRUD Avatar END

# Stages block
@api_view(['POST'])
def getStages(request):
    """
    Получение описания этапа

    :param request:
    :return:
    """
    eventId = int(request.data['EventId'])
    response = stageService.getStages(eventId)
    return response


@api_view(['PUT'])
def createStage(request):
    """
    Создание этапа

    :param request:
    :return:
    """
    userId = request.user.id
    eventId = request.data['EventId']
    if (eventService.checkAuthor(eventId=eventId, userId=userId)):
        response = stageService.createStage(request.data)
        return response
    else:
        return Response(data="Нет прав доступа", status=400)


@api_view(['POST'])
def updateStage(request):
    """
    Обновление данных по этапу

    :param request:
    :return:
    """
    userId = request.user.id
    eventId = request.data['EventId']
    if (eventService.checkAuthor(eventId=eventId, userId=userId)):
        response = stageService.updateStage(request.data)
        return response
    else:
        return Response(data="Нет прав доступа", status=400)


@api_view(['POST'])
def removeStage(request):
    """
    Удалить этап мероприятия

    :param request:
    :return:
    """
    userId = request.user.id
    eventId = request.data['EventId']
    stageId = request.data['StageId']
    if (eventService.checkAuthor(eventId=eventId, userId=userId)):
        response = stageService.removeStage(eventId, stageId)
        return response
    else:
        return Response(data="Нет прав доступа", status=400)


# Stages block END


# Fields block START

@api_view(['POST'])
def updateFields(request):
    """
    Обновление дополнительных полей регистрации этапа

    :param request:
    :return:
    """
    response = Response()
    try:
        userId = request.user.id
        stageId = request.data['StageId']
        fields = request.data['Fields']
        eventId = request.data['EventId']
        if (eventService.checkAuthor(eventId=eventId, userId=userId)):
            data, status = stageService.updateFields(stageId, fields)
            response = fillResponse(response, data, status)
        else:
            response = fillResponse("Нет прав доступа", 400)
    except BaseException:
        response = fillResponse(response, "Произошла ошибка при изменении дополнительных полей")
    return response


# Fields block END

# Registrations block START


@api_view(['POST'])
def registerUserToEvent(request):
    """
    Зарегистрировать участника на этап мероприятия

    :param request:{ EventId: int, StageId: int, Fields: JSON}.
        EventId: int,
        StageId: int,
        Fields: JSON,
    :return:
        200 - success
    """
    user = request.user
    response = Response()
    try:
        data, status = registrationService.registerUser(request.data, user)
        response = fillResponse(response, data, status)
    except BaseException:
        response = fillResponse(response, "Произошла ошибка при регистрации участника на мероприятие")
    return response


@api_view(['POST'])
def getAllRegistrations(request):
    """
    Получение всех мероприятий, на которые зарегистрирован участник

    :param request:
    :return:
    """
    pass


# Registration block END

@api_view(['GET'])
def getFormats(request):
    """
    Получение всех форматов проведения этапов

    :param request:
    """
    response = stageService.getFormats()
    return response


# Analytics block START

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getParticipants(request):
    """
    Получение списков участников на мероприятие

    :param request(EventId):
    :return список участников:
    """
    response = Response()
    try:
        eventId = request.data['EventId']
        userId = request.user.id
        data, status = registrationService.getParticipants(eventId, userId)
        response = fillResponse(response, data, status)
    except BaseException:
        response = fillResponse(response, "Произошла ошибка при получении списка участников", 400)
    return response


@api_view(['POST'])
def getListParticipants(request):
    pass


@api_view(['POST'])
def getAnalytics(request):
    """
    Получить аналитику по мероприятию

    :param countParticipants: количество участников
    :param countMan: количество мужчин
    :param countWoman: количество женщин
    :param ageGroups: [{ age: возраст, count: количество участников }]
    :param request:
    :return:
    """
    response = Response()
    try:
        eventId = request.data['EventId']
        userId = request.user.id
        data, status = registrationService.getAnalytics(eventId, userId)
        response = fillResponse(response, data, status)
    except BaseException:
        response = fillResponse(response, "Произшла внутренняя ошибка", 404)
    return response

# Analytics block END
