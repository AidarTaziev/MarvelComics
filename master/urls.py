from django.urls import path
from .views import SavedComicsList, SavedComicDetail

urlpatterns = [
    path('', SavedComicsList.as_view(), name='master'),
    path('comic/<int:pk>/', SavedComicDetail.as_view(), name='master_comic'),
]
