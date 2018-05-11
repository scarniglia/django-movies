from django.db import models
from django.urls import reverse

from .utils import to_roman

# Create your models here.
"""
Person
    Id
    Last Name
    First Name
    Aliases
    Movies as Actor/Actress
    Movies as Director
    Movies as Producer

Movie
    Id
    Title
    Release Year
    Casting (Actors + Actresses)
    Directors
    Producers

"""

GENDER_CHOICES = [('female', 'Female'), ('male', 'Male')]

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    aliases = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('first_name', 'last_name',)
    
    def __str__(self):
        title = '{} {}'.format(self.first_name, self.last_name,)
        if self.aliases:
            title = '{} ({})'.format(title, self.aliases)
        return title
    
    def get_absolute_url(self):
        return reverse('movies:person-detail', kwargs={'pk': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
        
    def get_absolute_url(self):
        return reverse('movies:category', kwargs={'pk': self.pk})

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    casting = models.ManyToManyField(Person, related_name='actor_movies')
    directors = models.ManyToManyField(Person, related_name='director_movies')
    producers = models.ManyToManyField(Person, related_name='producer_movies')
    categories = models.ManyToManyField(Category, related_name='movies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-release_year',)
    
    def __str__(self):
        return self.title
    
    def roman_release_year(self):
        """Roman representation of the release year"""
        return to_roman(self.release_year)
        
    
    def get_absolute_url(self):
        return reverse('movies:movie-detail', kwargs={'pk': self.pk})