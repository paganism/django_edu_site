from django.urls import path
from . import views

app_name = 'learn_it'

urlpatterns = [
    path('', views.index, name='index'),
    path('courses', views.CourseListView.as_view(), name='course-list'),
    path('course/<pk>', views.course_detail, name='course'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course-create'),
    path('courses/update/<pk>', views.CourseUpdateView.as_view(), name='course-update'),
    path('courses/delete/<pk>', views.CourseDeleteView.as_view(), name='course-delete'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login-user'),
]