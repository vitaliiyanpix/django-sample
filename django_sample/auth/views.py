from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserCreateView(generics.CreateAPIView):
    """Create a new user instance."""

    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        user = serializer.save()
        return user

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        data = serializer.data
        headers = self.get_success_headers(data)
        tokens = get_tokens_for_user(user)
        data['refresh_token'] = tokens.get('refresh')
        data['access_token'] = tokens.get('access')
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


