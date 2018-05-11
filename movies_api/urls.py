from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from movies_api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'persons', views.PersonViewSet)
router.register(r'movies', views.MovieViewSet)
router.register(r'categories', views.CategoryViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]