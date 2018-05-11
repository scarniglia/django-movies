# django-movies

This is just an example project

[Here is a working demo](https://movies.santic.me/)

## Configuration

settings.py
```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'movies.apps.MoviesConfig',
    'movies_api.apps.MoviesApiConfig',
    'widget_tweaks',
]

...
...
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

LOGOUT_REDIRECT_URL = '/'

LOGIN_REDIRECT_URL = '/'
```
urls.py
```
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^', include('movies.urls')),
    url(r'^api/', include('movies_api.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='movies/login.html',
    ), name='login'),
    path('admin/', admin.site.urls),
]
```