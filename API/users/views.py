from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import get_user_model

from .serializers import UserSerializer

Users = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]