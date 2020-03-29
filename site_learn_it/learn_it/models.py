from django.db import models
from site_learn_it import settings
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUser(AbstractUser):
    """Обучающийся и преподаватель"""

    USER_TYPE_CHOICE = (
        ('s', 'Student'),
        ('t', 'Teacher')
    )
    role = models.CharField('роль', max_length=1, choices=USER_TYPE_CHOICE, default='s', help_text='Выберите свою роль')

    objects = UserManager()

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.get_full_name}"

    def get_all_courses(self):
        courses_qs = Course.objects.filter(students=self.id)
        return [x.title for x in courses_qs]


class Days(models.Model):

    DAYS = (
        (1, "Понедельник"),
        (2, "Вторник"),
        (3, "Среда"),
        (4, "Четверг"),
        (5, "Пятница"),
        (6, "Суббота"),
        (7, "Воскресенье")
    )

    day = models.CharField('день недели', max_length=256, null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.day}'


class Course(models.Model):
    """Курс: python, java, экономика математика и т.д."""

    title = models.CharField('название', max_length=200)
    duration = models.CharField('продолжительность', max_length=50)
    about = models.TextField('о курсе', max_length=1000, null=True, blank=True)
    course_pic = models.ImageField( null=True, blank=True)
    students = models.ManyToManyField(CustomUser, related_name='courses', blank=True)
    date_start = models.DateField(auto_now_add=True, editable=True)
    
    day = models.ManyToManyField(Days, related_name='days')

    def __str__(self):
        return f"{self.title}"

    def get_short_description(self):
        return self.about [:70]


    # TODO Добавить функцию date_finish (date_start + duration)
    # TODO Добавить функцию is_active (date_finish - today)
