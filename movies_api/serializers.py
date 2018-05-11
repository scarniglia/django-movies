from rest_framework import serializers
from movies.models import Person, Movie, Category

class CategorySerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='movie-detail',
        queryset=Movie.objects.all(),
    )
    
    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'movies',)

class PersonSerializer(serializers.ModelSerializer):
    actor_movies = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='movie-detail',
        queryset=Movie.objects.all(),
    )
    director_movies = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='movie-detail',
        queryset=Movie.objects.all(),
    )
    producer_movies = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='movie-detail',
        queryset=Movie.objects.all(),
    )
    
    class Meta:
        model = Person
        fields = ('url', 'id', 'first_name', 'last_name', 'aliases', 'gender',
                  'actor_movies', 'director_movies', 'producer_movies',)

class MovieSerializer(serializers.ModelSerializer):
    roman_release_year = serializers.ReadOnlyField()
    categories = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='category-detail',
        queryset=Category.objects.all(),
    )
    casting = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='person-detail',
        queryset=Person.objects.all(),
    )
    directors = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='person-detail',
        queryset=Person.objects.all(),
    )
    producers = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='person-detail',
        queryset=Person.objects.all(),
    )

    class Meta:
        model = Movie
        fields = ('url', 'id', 'title', 'release_year', 'roman_release_year', 
                  'categories', 'casting', 'directors', 'producers',)