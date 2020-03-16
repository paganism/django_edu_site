from django.shortcuts import render

from django.contrib.auth.models import Group
from learn_it.models import CustomUser, Course
from rest_framework import viewsets
from rest_framework import permissions, generics
from .serializers import UserSerializer, GroupSerializer, CourseSerializer

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


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
