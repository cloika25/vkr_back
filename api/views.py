from rest_framework.response import Response
from rest_framework.decorators import api_view
import Serices.authService as authService
import Serices.eventService as eventService
import Serices.stagesService as stageService
import Serices.registrationService as registrationService
import json


@api_view(['GET'])
def allUsers(request):
    response = authService.getAllUsers()
    return Response(response.data)


# PersonaData block
@api_view(['GET'])
def getPersonalData(request):
    response = authService.getPersonalData(request.user)
    return response


@api_view(['POST'])
def editPersonalData(request):
    data = json.loads(request.read())
    body = data['body']
    response = authService.editPersonalData(request.user, body)
    return response


@api_view(['POST'])
def getName(request):
    data = request.data['id']
    response = authService.getName(data)
    return response


# PersonalData block END

# CRUD EVENTS
@api_view(['GET'])
def allEvents(request):
    response = eventService.getAllEvents()
    return response


@api_view(['GET'])
def myEvents(request):
    response = eventService.getUserEvents(request.user)
    return Response(response)


@api_view(['POST'])
def createEvent(request):
    data = json.loads(request.read())
    FullName = data['FullName']
    DateStart = data['DateStart']
    DateClose = data['DateClose']
    response = eventService.createEvent(request.user, FullName, DateStart, DateClose)
    return response


@api_view(['POST'])
def removeEvent(request):
    data = json.loads(request.read())
    id = data['id']
    response = eventService.removeEvent(id)
    return response


@api_view(['PUT'])
def updateEvent(request):
    data = request.data
    response = eventService.updateEvent(data)
    return response


@api_view(['POST'])
def getEvent(request):
    data = json.loads(request.read())
    id = data['id']
    response = eventService.getEvent(id)
    return response


@api_view(['POST'])
def getEventForEdit(request):
    data = json.loads(request.read())
    id = data['id']
    userId = request.user.id
    response = eventService.getEventForEdit(id, userId)
    return response


# CRUD Events END


# CRUD AVATAR
@api_view(['GET'])
def getAvatar(request):
    userId = request.user.id
    response = authService.getAvatar(userId)
    return response


@api_view(['POST'])
def updateAvatar(request):
    photo = request.data['photo']
    userId = request.user.id
    response = authService.updateAvatar(photo, userId)
    return response


@api_view(['GET'])
def removeAvatar(request):
    userId = request.user.id
    response = authService.removeAvatar(userId)
    return response


# CRUD Avatar END

# Stages block
@api_view(['POST'])
def getStages(request):
    eventId = int(request.data['EventId'])
    response = stageService.getStages(eventId)
    return response


@api_view(['PUT'])
def createStage(request):
    userId = request.user.id
    eventId = request.data['EventId']
    if (eventService.checkAuthor(eventId=eventId, userId=userId)):
        response = stageService.createStage(request.data)
        return response
    else:
        return Response(data="Нет прав доступа", status=400)


@api_view(['POST'])
def updateStage(request):
    userId = request.user.id
    eventId = request.data['EventId']
    if (eventService.checkAuthor(eventId=eventId, userId=userId)):
        response = stageService.updateStage(request.data)
        return response
    else:
        return Response(data="Нет прав доступа", status=400)


@api_view(['POST'])
def removeStage(request):
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
def getFields(request):
    stageId = request.data['StageId']
    response = stageService.getFields(stageId)
    return response


@api_view(['POST'])
def addFields(request):
    stageId = request.data['StageId']
    fields = request.data['Fields']
    response = stageService.addFields(stageId, fields)
    return response


@api_view(['POST'])
def updateFields(request):
    userId = request.user.id
    stageId = request.data['StageId']
    fields = request.data['Fields']
    eventId = request.data['EventId']
    if (eventService.checkAuthor(eventId=eventId, userId=userId)):
        response = stageService.updateFields(stageId, fields)
        return response
    else:
        return Response(data="Нет прав доступа", status=400)


# Fields block END

# Registrations block START


@api_view(['POST'])

def registerUserToEvent(request):
    """Зарегистрировать участника на этап мероприятия

    :param request:
        EventId: int,
        StageId: int,
        Fields: JSON,
    :return:
        200 - success
    """
    user = request.user
    response = registrationService.registerUser(request.data, user)
    return response


@api_view(['POST'])
def getAllRegistrations(request):
    pass


# Registration block END

@api_view(['GET'])
def getFormats(request):
    response = stageService.getFormats()
    return response

# Analytics block START

@api_view(['POST'])
def getParticipants(request):
    eventId = request.data['EventId']
    userId = request.user.id
    response = registrationService.getParticipants(eventId, userId)
    return response

@api_view(['POST'])
def getListParticipants(request):
    pass

@api_view(['POST'])
def getAnalytics(request):
    pass

# Analytics block END
