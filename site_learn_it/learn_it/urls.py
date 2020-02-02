from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses', views.CourseListView.as_view(), name='course-list'),
    path('course/<pk>', views.course_detail, name='course'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login-user'),
]