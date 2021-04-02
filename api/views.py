from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
import Serices.authService as authService
import Serices.eventService as eventService
import json

@api_view(['GET'])
def allUsers(request):
    response = authService.getAllUsers()
    return Response(response.data)

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

@api_view(['GET'])
def all_events(request):
    response = eventService.getAllEvents()
    return response

@api_view(['GET'])
def my_events(request):
    response = eventService.getUserEvents(request.user)
    return Response(response)

@api_view(['POST'])
def create_event(request):
    data = json.loads(request.read())
    FullName = data['FullName']
    DateStart = data['DateStart']
    DateClose = data['DateClose']
    response = eventService.createEvent(request.user, FullName, DateStart, DateClose)
    return response

@api_view(['POST'])
def remove_event(request):
    data = json.loads(request.read())
    id = data['id']
    response = eventService.removeEvent(id)
    return response

@api_view(['PUT'])
def update_event(request):
    data = request.data
    response = eventService.updateEvent(data)
    return response

@api_view(['POST'])
def get_event(request):
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

@api_view(['POST'])
def getName(request):
    data = request.data['id']
    response = authService.getName(data)
    return response

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