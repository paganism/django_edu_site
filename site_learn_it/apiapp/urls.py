from django.urls import path, include
from .views import UserViewSet, CourseViewSet, GroupList, LoginView


urlpatterns = [
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path("token/", include('oauth2_provider.urls', namespace='token')),
    path("users/", UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='apiusers'),
    path("users/<pk>", UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
    path("groups/", GroupList.as_view()),
    path("courses/", CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='apicourses'),
    path("courses/<pk>", CourseViewSet.as_view({'get': 'retrieve'})),
    path("login/", LoginView.as_view(), name="login"),
    ]
