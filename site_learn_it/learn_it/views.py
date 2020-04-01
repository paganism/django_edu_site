from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from .models import Course, CustomUser, Days
from django.utils import timezone
from .forms import RegistrationForm, LoginForm, ContactForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.template.context_processors import csrf
from .tasks import send_mail_from_form

from datetime import timedelta
from django.utils import timezone

from django.db.models import Q, F, Max, Min, Exists, OuterRef, Sum, Count, Subquery


def index(request):
    return render(request, 'learn_it/index.html')


class CourseListView(ListView):

    model = Course
    paginate_by = 50  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['now'] = timezone.now()
        return context



def course_detail(request, pk):
    """детали курса"""
    course_data = Course.objects.get(id=pk)
    days = Days.objects.filter(days__id=pk)
    context = {'course': course_data, 'days': days}

    if request.method == 'GET':
        return render(request, 'learn_it/course_detail.html', context)

    if request.method == 'POST':
        
        if request.POST.get('subscribe') == 'del':
            course_data.students.remove(request.user)
        else:
            course_data.students.add(request.user)

        return render(request, 'learn_it/course_detail.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
        return render(request, 'registration/register.html', {'form': form})
    else:
        form = RegistrationForm()
        
        return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('learn_it:course-list')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'learn_it/course_create_form.html'
    success_url = reverse_lazy('learn_it:course-list')
    fields = ['title', 'duration', 'about', 'course_pic', 'day',]


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    template_name = 'learn_it/course_create_form.html'
    success_url = reverse_lazy('learn_it:course-list')
    fields = ['title', 'duration', 'about', 'course_pic', 'day',]


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('learn_it:course-list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser,
                     login_url=reverse_lazy('learn_it:login-user')))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ContactsView(View):
    template_name = 'learn_it/contacts.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context.update(csrf(request))
        context['contact_form'] = ContactForm()

        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = ContactForm(request.POST)


        if form.is_valid():

            email_body = f"{form.cleaned_data['message']}"
            email_to_answer = f"{form.cleaned_data['email']}"

            # call celery task
            send_mail_from_form.delay(email_to_answer, email_body)

        return render(request, template_name=self.template_name, context=context)


class StatisticsView(View):
    template_name = 'learn_it/statistics.html'

    def get(self, request, *args, **kwargs):
        context = {}

        one_month_ago = timezone.now() - timedelta(days=30)

        popular_courses_in_month = Course.objects.filter(
            Exists(CustomUser.objects.filter(courses=OuterRef('pk'), date_joined__gte=one_month_ago)))
        context['popular_courses_in_month'] = popular_courses_in_month

        popular_courses = Course.objects.values('title').annotate(count=Count('students')).order_by('-count')[:10]

        context['popular_courses'] = popular_courses
        context['most_popular'] = popular_courses.first()

        longest_duration = Course.objects.all().aggregate(Max('duration'))
        longest_course = Course.objects.get(duration=longest_duration['duration__max'])
        context['longest_course'] = longest_course

        busiest_days = Course.objects.values('day').annotate(count=Count('day')).order_by('-count')
        context['busiest_days'] = busiest_days

        return render(request, template_name=self.template_name, context=context)
