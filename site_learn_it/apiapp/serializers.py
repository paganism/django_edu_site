from django.contrib.auth.models import Group
from learn_it.models import CustomUser, Course
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'email', 'groups', 'role']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'duration', 'date_start', 'students', ]
