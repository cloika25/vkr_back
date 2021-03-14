from django.contrib.auth import authenticate, login
from Serializers.Users import *

def getAllUsers():
    allUsers = User.objects.all()
    allUsersSerial = UserSerializer(allUsers, many= True)
    return allUsersSerial

def authen(username, password, request):
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
    result = { 'username': user.username }
    return result

def registration(username, password):
    result = {
        'data': '',
        'code': '',
    }
    try:
        user = User.objects.filter(username=username)
        if user:
            print(Exception.__class__)
            result['data'] = "Данный логин уже используется"
            result['code'] = 400
        else:
            user = User.objects.create_user(username=username, password= password)
            user.save()
            result['data'] = "Пользователь создан"
            result['code'] = 200
    except Exception:
        result['data'] = "Что-то пошло не так"
        result['code'] = 400

    return result