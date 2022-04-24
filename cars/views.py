from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from itsdangerous import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
        'Update Car Record': '/updateCars',
        'Fetch All Cars': '/fetchCars',
    }
    return Response(api_urls)

@api_view(['POST'])
def addCars(request):
    car_serializer = CarSerializer(data = request.data)
    if car_serializer.is_valid():
        if Car.objects.filter(email=request.data['email']).exists():
            raise Serializer.ValidationError("Email Already Exists")
        else:
            car_serializer.save()
            return Response(car_serializer.data)
    else:
        return Response({"error":car_serializer.errors, "data":car_serializer.data}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def fetchCars(request):
    # checking for the parameters from the URL
    if request.query_params:
        cars = Car.objects.filter(**request.query_params.dict())
    else:
        cars = Car.objects.all()
    if cars:
        return Response(CarSerializer(cars, many=True).data)
    else:
        return Response("No Car records found")

@api_view(['POST'])
def updateCars(request, pk):
    car = Car.objects.get(id=pk)
    update_car_data = CarSerializer(instance=car, data=request.data)

    if update_car_data.is_valid():
        update_car_data.save()
        return Response(update_car_data.data)
    else:
        return Response(update_car_data.errors)

@api_view(['DELETE'])
def deleteCar(request, pk):
    car = get_object_or_404(Car, id=pk)
    car.delete()
    return Response(status=status.HTTP_202_ACCEPTED)