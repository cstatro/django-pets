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

    @staticmethod
    def update(instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.favorite_food = validated_data.get(
            'favorite_food', instance.favorite_food)
        instance.save()
        return DogSerializer(instance).data

    @staticmethod
    def destroy(instance):
        dead_dog = instance.delete()
        return DogSerializer(instance).data
