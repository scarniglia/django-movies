from django.forms import ModelForm

from .models import Movie, Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'aliases', 'gender',]

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_year', 'categories',
                  'casting', 'directors', 'producers',]