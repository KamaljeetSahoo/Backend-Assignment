import email
from django.http import HttpResponse
from itsdangerous import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Car
from .serlializers import CarSerializer

# Create your views here.
def test_view(request):
    return HttpResponse("<h1>Hello</h1>")

@api_view(['GET'])
def CarApiOverview(request):
    api_urls = {
        'OverView API endpoints' : '/',
        'Add Car': '/addCar',
    }
    return Response(api_urls)

@api_view(['POST'])
def addCars(request):
    car = CarSerializer(data = request.data)
    if car.is_valid():
        if Car.objects.filter(email=request.data['email']).exists():
            raise Serializer.ValidationError("Email Already Exists")
        else:
            car.save()
            return Response(car.data)
    else:
        return Response({"error":car.errors, "data":car.data}, status=status.HTTP_404_NOT_FOUND)