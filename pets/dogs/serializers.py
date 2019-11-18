from rest_framework import serializers
from .models import Dog
from datetime import date


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('id', 'name', 'favorite_food')

    def create(self, validated_data):
        dog = Dog.objects.create(**validated_data)
        return DogSerializer(dog).data
