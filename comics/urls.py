from django.urls import path, include
from .views import SearchComics, Comic


urlpatterns = [
    path('', SearchComics.as_view(), name='search_comics'),
    path('comic/<int:id>', Comic.as_view(), name='comic'),
]