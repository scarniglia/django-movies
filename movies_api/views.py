from rest_framework import permissions
from rest_framework import viewsets

from movies.models import Person, Movie, Category
from movies_api.serializers import (
    PersonSerializer,
    MovieSerializer,
    CategorySerializer,
)

class PersonViewSet(viewsets.ModelViewSet):
    """
    This viewset provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Person
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MovieViewSet(viewsets.ModelViewSet):
    """
    This viewset provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Movie
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer