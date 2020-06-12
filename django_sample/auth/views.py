from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from . import serializers


class UserCreateView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing users.

    post:
    Create a new user instance.
    """

    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

