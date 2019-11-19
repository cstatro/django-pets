from django.urls import path
from .views import DogList, DogShow


urlpatterns = [
    path('dogs/', DogList.as_view()),
    path('dog/<int:num>', DogShow.as_view()),
]
