from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
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
    response =  authService.authen(login, password, request)
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

@api_view(['POST'])
def update_event(request):
    data = json.loads(request.read())
    pass

@api_view(['POST'])
def get_event(request):
    data = json.loads(request.read())
    id = data['id']
    token = Token.objects.create(user = ... )
    response = eventService.getEvent(id)
    return Response(data=response['data'], status=response['status'])