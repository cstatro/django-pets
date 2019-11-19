from django.urls import path
from .views import DogList


urlpatterns = [
    path('dogs/', DogList.as_view())
]
