from api.models import Event
def fillResponse(response , data = '', statusCode = 404):
    response.data = data
    response.status_code = statusCode
    return response

def isCreator(eventId, userId):
    result = Event.objects.filter(id=eventId, AuthorUserId=userId).count()
    return result