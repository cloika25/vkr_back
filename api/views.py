from rest_framework.response import Response
from rest_framework.decorators import api_view
import Serices.authService as authService
import Serices.eventService as eventService
import json

@api_view(['GET'])
def allUsers(request):
    response = authService.getAllUsers()
    return Response(response.data)

@api_view(['POST'])
def login(request):
    data = json.loads(request.read())
    login = data['login']
    password = data['password']
    response =  authService.authen(login, password)
    return Response(response)

@api_view(['POST'])
def registration(request):
    data = json.loads(request.read())
    login = data['login']
    password = data['password']
    response = authService.registration(login, password)
    Response(response)

@api_view(['GET'])
def all_events(request):
    response = eventService.getAllEvents()
    return Response(response)

@api_view(['POST'])
def create_event(request):
    data = json.loads(request.read())
    FullName = data['FullName']
    DateStart = data['DateStart']
    DateClose = data['DateClose']
    response = eventService.createEvent(FullName, DateStart, DateClose)
    return Response(data=response['data'], status=response['status'])

@api_view(['POST'])
def remove_event(request):
    data = json.loads(request.read())
    id = data['id']
    response = eventService.removeEvent(id)
    return Response(data=response['data'], status=response['status'])
