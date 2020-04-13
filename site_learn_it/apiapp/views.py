from django.shortcuts import render

from django.contrib.auth.models import Group
from learn_it.models import CustomUser, Course
from rest_framework import viewsets
from rest_framework import permissions, generics, status
from .serializers import UserSerializer, GroupSerializer, CourseSerializer
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from site_learn_it import settings

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]


# class UserList(generics.ListCreateAPIView):
#     queryset = CustomUser.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#
#
# class UserDetails(generics.RetrieveAPIView):
#     queryset = CustomUser.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]


class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all().order_by('-date_start')
    serializer_class = CourseSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")

        token = self.get_token(username=username, passw=password)
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": token['access_token']})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

    def get_token(self, username, passw):
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'authorization': settings.BASIC_AUTH
        }
        payload = {'grant_type': 'password', 'username': username, 'password': passw, }
        token = requests.post('http://localhost:8000/api-oauth/o/token/', data=payload, headers=headers)
        return token.json()
