from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import DogSerializer
from .models import Dog
from rest_framework.response import Response
# Create your views here.


class DogList(APIView):
    def get(self, request, format=None):
        dogs = Dog.objects.all()
        serialized_dogs = DogSerializer(dogs, many=True)
        return Response(serialized_dogs.data)

    def post(self, request, format=None):
        serializer = DogSerializer()
        dog = serializer.create(request.data)
        return Response(dog)
