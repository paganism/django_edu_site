from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APISimpleTestCase, APITransactionTestCase, APIRequestFactory

from learn_it.models import Course, CustomUser
from .views import CourseViewSet
from .factories import CourseFactory, UserFactory
from rest_framework.test import force_authenticate

from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token
from oauth2_provider.models import AccessToken, Application
from django.utils.timezone import now, timedelta


class TestCaseForCourseSimple(APISimpleTestCase):
    def test_create_course_request_factory(self):
        course = CourseFactory.build(title='TestCourse', duration=5, about='test descr')
        self.assertEqual(course.title, 'TestCourse')


class TestCaseForCourse(APITestCase):

    def setUp(self):
        self.user = UserFactory(username='vasya', password='vasya')

    def test_get_courses_request_factory(self):
        course = CourseFactory(title='TestCourse', duration=5, about='test descr')
        request_factory = APIRequestFactory()
        request = request_factory.get("/api-oauth/courses/")

        course_view = CourseViewSet.as_view({'get': 'list'})

        force_authenticate(request, user=self.user)

        response = course_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.count(), 1)

    def test_post_course_request_factory(self):
        request_factory = APIRequestFactory()
        request = request_factory.post("/api-oauth/courses/",  {"title": "TestCourse",
                                                                "duration": 1,
                                                                'about': 'test descr'}, format="json")
        course_view = CourseViewSet.as_view({'post': 'create'})

        force_authenticate(request, user=self.user)

        response = course_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_negative_get_courses_request_factory(self):
        course = CourseFactory(title='TestCourse', duration=5, about='test descr')
        request_factory = APIRequestFactory()
        request = request_factory.get("/api-oauth/courses/")

        course_view = CourseViewSet.as_view({'get': 'list'})

        response = course_view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Course.objects.get(title='TestCourse').title, 'TestCourse')


class TestCaseForUsersTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory(username='nikola', password='solvo2solvo')
        cls.user.set_password('solvo2solvo')
        cls.user.save()

        cls.app = Application(
            client_type='confidential',
            authorization_grant_type='password',
            name='MyAppTest',
            user_id=1
        )
        cls.app.save()

        cls.app = Application.objects.get(name='MyAppTest')
        cls.token = generate_token()
        cls.expires = now() + timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)
        cls.scope = 'read write'
        cls.access_token = AccessToken.objects.create(
            user=cls.user,
            application=cls.app,
            expires=cls.expires,
            token=cls.token,
            scope=cls.scope
        )

    def test_can_read_user_list(self):
        self.client.force_authenticate(user=self.user, token=self.access_token)
        response = self.client.get(reverse('apiusers'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_negative_can_read_user_list(self):
        response = self.client.get(reverse('apiusers'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_read_direct_user(self):
        self.client.force_authenticate(user=self.user, token=self.access_token)
        response = self.client.get(reverse('user-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'nikola')

    def test_can_create_user(self):
        self.client.force_authenticate(user=self.user, token=self.access_token)

        url = reverse('apiusers')
        data = {'username': 'testcreateuser'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # initial user + created user = 2
        self.assertEqual(CustomUser.objects.count(), 2)
        self.assertEqual(CustomUser.objects.get(username='testcreateuser').username, 'testcreateuser')


class TestCaseForCoursesTransactional(APITransactionTestCase):

    @classmethod
    def setUpClass(cls):
        cls.course = CourseFactory(title='TestCourseTrans', duration=6, about='test descr')
        cls.user = UserFactory(username='kolya', password='kolya')

    def test_count_courses_transactional(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('apicourses')
        data = {'title': 'TestCourseTrans1', 'duration': 7, 'about': 'test descr1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # initial user + created user = 2
        self.assertEqual(Course.objects.count(), 2)
        self.assertEqual(Course.objects.get(title='TestCourseTrans1').title, 'TestCourseTrans1')

    def test_count_zero_courses(self):
        # after previous transaction count shoud be 0
        self.assertEqual(Course.objects.count(), 0)

    @classmethod
    def tearDownClass(cls):
        pass
