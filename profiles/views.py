from django.core.cache import cache
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from profiles.serializers import UserSerializer


@api_view(['POST'])
@permission_classes([])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Please provide both username and password.'},
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(username=username, password=password)
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
    except:
        return Response({'error': 'Unable to register user.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    tokens = OutstandingToken.objects.filter(user_id=request.user.id)
    for token in tokens:
        t, _ = BlacklistedToken.objects.get_or_create(token=token)
    cache.clear()
    request.session.flush()
    return Response(status=status.HTTP_205_RESET_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_username(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)
