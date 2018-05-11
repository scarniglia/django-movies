from django.shortcuts import render
from django.views.generic import ListView, DeleteView

from .models import Movie, Person

class MoviesList(ListView):
    model = Movie
    template_name = 'movies/index.html'
    context_object_name = 'movies'
    
    
    def get_queryset(self):
        qs = self.model.objects.all()
        category_id = self.kwargs.get('category_id', None)
        if category_id: 
            qs = qs.filter(categories__id=category_id)
        q = self.request.GET.get('q', None)
        if q: 
            qs = qs.filter(title__icontains=q)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

class PersonList(ListView):
    model = Person
    template_name = 'movies/person_list.html'
    context_object_name = 'persons'
    
    
    def get_queryset(self):
        qs = self.model.objects.all()
        role = self.kwargs.get('role', None)
        if role == 'actors':
            qs = qs.filter(actor_movies__isnull=False)
        if role == 'directors':
            qs = qs.filter(director_movies__isnull=False)
        if role == 'producers':
            qs = qs.filter(producer_movies__isnull=False)
        return qs

class DeleteView(DeleteView):

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)