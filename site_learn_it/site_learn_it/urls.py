from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import settings
from django.conf.urls.static import static

from rest_framework import routers
from apiapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'courses', views.CourseViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('learn_it/', include('learn_it.urls')),
    path('', RedirectView.as_view(url='/learn_it/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-oauth/', include('apiapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns 

urlpatterns += [
    path('django-rq/', include('django_rq.urls'))
]
