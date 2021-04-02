def fillResponse(response , data = '', statusCode = 404):
    response.data = data
    response.status_code = statusCode
    return response