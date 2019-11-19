from django.test import TestCase
from .serializers import DogSerializer
from .models import Dog
# Create your tests here.


class DogTest(TestCase):
    def setUp(self):
        dog_one = dict(name="jimmy", favorite_food="kibble")
        serializer = DogSerializer()
        serializer.create(dog_one)

    def test_dog_one(self):
        """finds jimmy as the first dog"""
        name = Dog.objects.first().name
        self.assertEqual(name, "jimmy")
