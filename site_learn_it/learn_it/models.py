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
    
    day = models.ManyToManyField(Days, related_name='courses')

    def __str__(self):
        return f"{self.title}"

    def get_short_description(self):
        return self.about [:70]


    # Добавить функцию date_finish (date_start + duration)
    # Добавить функцию is_active (date_finish - today)


class Lesson(models.Model):
    """Одно зантие в расписании."""

    TIMESLOTS_SCHEDULE = [
        "16:00-16:40",
        "16:50-17:30",
        "17:40-18:20",
        "18:35-19:15",
        "19:25-20:05"
    ]

    course = models.ForeignKey(Course, null=True, verbose_name='курс', on_delete=models.CASCADE)
    teacher = models.ForeignKey(CustomUser, null=True, verbose_name='преподаватель', on_delete=models.CASCADE)

    timeslot = models.IntegerField('слот', db_index=True, help_text='Номер слота в расписании')
    room = models.CharField('класс', db_index=True, help_text='Класс где проходят занятия.', max_length=50)
    date = models.DateField('дата', db_index=True)

    def __str__(self):
        return f"{self.course.title}"


class Mark(models.Model):
    """Отметка о прохождении курса"""
    points = models.IntegerField('оценка')
    teacher_note = models.TextField('комментарий', null=True)
    created = models.DateField('дата')
    student = models.OneToOneField(CustomUser, verbose_name='студент', on_delete=models.CASCADE, related_name='student_mark')
    course = models.ForeignKey(Course, verbose_name='предмет', on_delete=models.CASCADE)
    teacher = models.OneToOneField(CustomUser, verbose_name='преподаватель', on_delete=models.CASCADE, related_name='teacher_mark')

    def __str__(self):
        return f"{self.points}"
