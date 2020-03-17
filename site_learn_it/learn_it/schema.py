import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Course, CustomUser


class CourseType(DjangoObjectType):

    class Meta:
        model = Course


class CourseFilteredType(DjangoObjectType):

    class Meta:
        model = Course

        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )


class CustomUserType(DjangoObjectType):

    class Meta:
        model = CustomUser


class CustomUserFilterType(DjangoObjectType):

    class Meta:
        model = CustomUser
        filter_fields = {
            'username': ['exact', 'icontains', 'istartswith', ],
            'role': ['exact', 'icontains', 'istartswith', ]
        }
        interfaces = (graphene.relay.Node, )


class CustomUserMutation(graphene.Mutation):

    class Arguments:
        user_id = graphene.Int(required=True)
        new_username = graphene.String(required=True)

    result = graphene.Boolean()
    user = graphene.Field(CustomUserType)

    def mutate(self, info, user_id, new_username):

        return {
            'result': True,
            'user': CustomUser.objects.first()
        }


class CourseMutation(graphene.Mutation):

    class Arguments:
        course_id = graphene.Int(required=True)
        new_title = graphene.String(required=True)

    result = graphene.Boolean()
    course = graphene.Field(CourseType)

    def mutate(self, info, course_id, new_title):

        return {
            'result': True,
            'course': Course.objects.first()
        }


class Mutation:
    change_course_name = CourseMutation.Field()
    change_customuser_name = CustomUserMutation.Field()


class Query:
    all_courses = graphene.List(CourseType, limit=graphene.Int())
    all_users = graphene.List(CustomUserType, limit=graphene.Int())
    all_students = graphene.List(CustomUserType, limit=graphene.Int())

    retrieve_course = graphene.Field(CourseType, id=graphene.Int())
    retrieve_user = graphene.Field(CustomUserType, id=graphene.Int())

    filtered_users = DjangoFilterConnectionField(CustomUserFilterType)
    filtered_courses = DjangoFilterConnectionField(CourseFilteredType)

    def resolve_all_courses(self, *args, **kwargs):
        if 'limit' in kwargs:
            return Course.objects.all()[:kwargs['limit']]
        return Course.objects.all()

    def resolve_all_users(self, *args, **kwargs):
        if 'limit' in kwargs:
            return CustomUser.objects.all()[:kwargs['limit']]
        return CustomUser.objects.all()

    def resolve_all_students(self, *args, **kwargs):
        if 'limit' in kwargs:
            return CustomUser.objects.filter(role="s")[:kwargs['limit']]
        return CustomUser.objects.filter(role="s")

    def resolve_retrieve_course(self, info, **kwargs):
        if 'id' in kwargs:
            return Course.objects.get(id=kwargs['id'])

    def resolve_retrieve_user(self, info, **kwargs):
        if 'id' in kwargs:
            return CustomUser.objects.get(id=kwargs['id'])