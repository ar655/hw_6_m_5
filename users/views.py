from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserLoginValidateSerializer,UserAddSerializer
from django.contrib.auth.models import User

@api_view(['POST'])
def register(request):
    serializer = UserAddSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_202_ACCEPTED)





@api_view(['POST'])
def login(request):
    # username = request.data.get('username')
    # password = request.data.get('password')
    serializer = UserLoginValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if user is not None:
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)