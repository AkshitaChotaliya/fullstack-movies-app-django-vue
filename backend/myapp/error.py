from rest_framework.response import Response
from rest_framework import status

def error_response(message, code=status.HTTP_400_BAD_REQUEST, errors=None):
    data = {
        "success": False,
        "message": message,
    }
    if errors:
        data["errors"] = errors
    return Response(data, status=code)

def not_found(message="Resource not found"):
    return error_response(message, code=status.HTTP_404_NOT_FOUND)

def forbidden(message="You are not allowed to do this"):
    return error_response(message, code=status.HTTP_403_FORBIDDEN)

def internal_error(message="Something went wrong"):
    return error_response(message, code=status.HTTP_500_INTERNAL_SERVER_ERROR)
