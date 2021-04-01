from django.contrib.auth import authenticate, login
from Serializers.Users import *
from rest_framework.response import Response

def getAllUsers():
    allUsers = User.objects.all()
    allUsersSerial = UserSerializer(allUsers, many= True)
    return allUsersSerial

def createProfile(user):
    try:
        newProfile = Profile(user=user)
        newProfile.save()
    except Exception:
        print('error while creating profile')

def getPersonalData(user):
    response = Response()
    profile = Profile.objects.filter(user_id=user.id)
    if (profile.count() == 0):
        createProfile(user)
        profile = Profile.objects.get(user_id=user.id)
    else:
        profile = profile.first()
    profile = CabinetSerializer(profile).data
    response.data = {
        "firstName": profile["user"]["first_name"],
        "lastName": profile["user"]["last_name"],
        "email": profile["user"]["email"],
        "genderId": profile["genderId"],
        "birthDate": profile["birth_date"],
        "photo": profile["photo"],
    }
    return response

def getName(data):
    response = Response()
    try:
        profile = Profile.objects.get(user_id=data)
        response.data = {
            "firstName": profile.user.first_name,
            "lastName": profile.user.last_name,
            "photo": profile.photo.name
        }
        response.status_code = 200
        return response
    except:
        response.data = "Произошла ошибка получение данных пользователя"
        response.status_code = 400
        return response

def editPersonalData(user, body):
    response = Response()
    try:
        tempUser = User.objects.get(id = user.id)
        tempUser.first_name = body['firstName']
        tempUser.last_name = body['lastName']
        tempUser.email = body['email']
        tempProf = Profile.objects.get(user_id= user.id)
        tempProf.genderId = body['genderId']
        tempProf.birth_date = body['birthDate']
        tempUser.save()
        tempProf.save()
        response.status_code = 200
        return response
    except Exception:
        response.status_code = 400
        response.data = "Произошла ошибка при изменении персональных данных"
        return response

def getAvatar(userId):
    response = Response()
    try:
        user = Profile.objects.get(user_id=userId)
        response.data = user.photo.name
        response.status_code = 200
    except:
        response.data = "Произошла ошибка при получаении аватара"
        response.status_code = 400
    return response

def updateAvatar(photo, userId):
    response = Response()
    try:
        if (photo != "undefined"):
            profile = Profile.objects.get(user_id=userId)
            profile.photo = photo
            profile.save()
            response.data = "Успешно обновлено"
            response.status_code = 200
        else:
            response.data = "Пришел undefined"
            response.status_code = 400
    except:
        response.data["Произошла ошибка при обновлении"]
        response.status_code = 400
    return response

def removeAvatar(userId):
    response = Response()
    try:
        profile = Profile.objects.get(user_id=userId)
        profile.photo = ''
        profile.save()
        response.data = "Все ок"
        response.status_code = 200
    except:
        response.data = "Произошла ошибка при удалении аватара"
        response.data = 400
    return response

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