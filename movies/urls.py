from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.urls import path
from django.views.generic import DetailView, CreateView, UpdateView

from . import views
from .models import Movie, Person
from .forms import MovieForm, PersonForm

app_name = 'movies'
urlpatterns = [
    url(r'^$', views.MoviesList.as_view(), name='index'),
    
    path('movies/create', login_required(CreateView.as_view(
        form_class = MovieForm,
        template_name = 'movies/movie_form.html',
    )), name='movie-create'),
    
    path('movie/<pk>/update/', login_required(UpdateView.as_view(
        form_class = MovieForm,
        model = Movie,
        template_name = 'movies/movie_form.html',
    )), name='movie-update'),
    
    path('movie/<pk>/delete/', login_required(views.DeleteView.as_view(
        model = Movie,
        success_url = reverse_lazy('movies:index')
    )), name='movie-delete'),
    
    path('persons/create', login_required(CreateView.as_view(
        form_class = PersonForm,
        template_name = 'movies/person_form.html',
    )), name='person-create'),
    
    path('person/<pk>/update/', login_required(UpdateView.as_view(
        form_class = PersonForm,
        model = Person,
        template_name = 'movies/person_form.html',
    )), name='person-update'),
    
    path('person/<pk>/delete/', login_required(views.DeleteView.as_view(
        model = Person,
        success_url = reverse_lazy('movies:persons')
    )), name='person-delete'),
    
    path('movie/<pk>/', DetailView.as_view(
        model = Movie,
        template_name = 'movies/movie_detail.html',
        context_object_name = 'movie',
    ), name='movie-detail'),
    
    path('person/<pk>/', DetailView.as_view(
        model = Person,
        template_name = 'movies/person_detail.html',
        context_object_name = 'person',
    ), name='person-detail'),
    
    url(r'^persons/$',
        views.PersonList.as_view(),
        name='persons'
        ),
    
    url(r'^persons/(?P<role>\w+)$',
        views.PersonList.as_view(),
        name='persons'
        ),
    
    url(r'^category/(?P<category_id>\d+)$',
        views.MoviesList.as_view(),
        name='category'
        ),
]