from django.contrib.auth import authenticate, login
from Serializers.Users import *
from rest_framework.response import Response
from .util import fillResponse


def getAllUsers():
    allUsers = User.objects.all()
    allUsersSerial = UserSerializer(allUsers, many=True)
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
    profile = ProfileSerializer(profile).data
    body = {
        "firstName": profile["user"]["first_name"],
        "lastName": profile["user"]["last_name"],
        "email": profile["user"]["email"],
        "username": profile["user"]["username"],
        "genderId": profile["genderId"],
        "birthDate": profile["birth_date"],
        "photo": profile["photo"],
    }
    response = fillResponse(response, body, 200)
    return response


def getName(data):
    response = Response()
    try:
        profile = Profile.objects.get(user_id=data)
        body = {
            "firstName": profile.user.first_name,
            "lastName": profile.user.last_name,
            "photo": profile.photo.name
        }
        response = fillResponse(response, body, 200)
        return response
    except:
        response = fillResponse(response, "Произошла ошибка получение данных пользователя", 400)
        return response


def editPersonalData(user, body):
    tempUser = User.objects.get(id=user.id)
    tempUser.first_name = body['firstName']
    tempUser.last_name = body['lastName']
    tempUser.email = body['email']
    tempProf = Profile.objects.get(user_id=user.id)
    tempProf.genderId = body['genderId']
    tempProf.birth_date = body['birthDate']
    tempUser.save()
    tempProf.save()
    return "Персональные данные успешно обновлены", 200


def getAvatar(userId):
    response = Response()
    try:
        user = Profile.objects.get(user_id=userId)
        response = fillResponse(response, user.photo.name, 200)
    except:
        response = fillResponse(response, "Произошла ошибка при получаении аватара", 400)
    return response


def updateAvatar(photo, userId):
    response = Response()
    try:
        if (photo != "undefined"):
            profile = Profile.objects.get(user_id=userId)
            profile.photo = photo
            profile.save()
            response = fillResponse(response, "Успешно обновлено", 200)
        else:
            response = fillResponse(response, "Пришел undefined", 400)
    except:
        response = fillResponse(response, "Произошла ошибка при обновлении", 400)
    return response


def removeAvatar(userId):
    response = Response()
    try:
        profile = Profile.objects.get(user_id=userId)
        profile.photo = ''
        profile.save()
        response = fillResponse(response, "Все ок", 200)
    except:
        response = fillResponse(response, "Произошла ошибка при удалении аватара", 400)
    return response
