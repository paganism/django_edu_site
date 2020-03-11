from django.urls import path, include
from .views import UserDetails, UserList, GroupList

# app_name = 'apiapp'
urlpatterns = [
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
    path("users/", UserList.as_view()),
    path("users/<pk>", UserDetails.as_view()),
    path("groups/", GroupList.as_view()),
    ]
