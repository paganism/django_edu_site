from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Course, CustomUser, Days
from django.utils import timezone
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login


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
    days = Days.objects.filter(courses__id=pk)
    context = {'course': course_data, 'days': days}

    if request.method == 'GET':
        return render(request, 'learn_it/course_detail.html', context)

    if request.method == 'POST':
        
        if request.POST.get('subscribe') == 'del':
            course_data.students.remove(request.user)
        else:
            course_data.students.add(request.user)
            course_data.save()

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
                return redirect('course-list')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})