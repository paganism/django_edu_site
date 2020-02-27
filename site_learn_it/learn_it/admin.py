from django.contrib import admin
from django import forms

from .models import Course, CustomUser 

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'get_short_description', 'date_start')
    list_filter = ('title', 'duration', )


@admin.register(CustomUser)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role', 'get_all_courses',)
    list_filter = ('username', 'first_name', 'last_name', 'role',)