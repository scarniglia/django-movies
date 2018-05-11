from django.contrib import admin

from .models import Person, Category, Movie

admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Movie)