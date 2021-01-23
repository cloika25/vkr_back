from django.contrib.auth import authenticate
from Serializers.Users import *

def getAllUsers():
    allUsers = User.objects.all()
    allUsersSerial = UserSerializer(allUsers, many= True)
    return allUsersSerial

def authentificate(login, password):
    user = authenticate(username = login, password = password)
    result = { 'username': user.username }
    return result

def registration(login, password):
    result = {
        'data': '',
        'code': '',
    }
    try:
        user = User.objects.filter(username=login)
        if user:
            print(Exception.__class__)
            result['data'] = "Данный логин уже используется"
            result['code'] = 400
        else:
            user = User.objects.create_user(username=login, password= password)
            user.save()
            result['data'] = "Пользователь создан"
            result['code'] = 200
    except Exception:
        result['data'] = "Что-то пошло не так"
        result['code'] = 400

    return result