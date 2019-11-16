from rest_framework import serializers
from dogs.models import Dog
from datetime import date


class DogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=255)
    birthday = serializers.DateField(default=date.today)

    def create(self, validated_data):
        return Dog.objects.create(**validated_data)
