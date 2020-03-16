import factory

from learn_it.models import Course, CustomUser


class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = CustomUser
