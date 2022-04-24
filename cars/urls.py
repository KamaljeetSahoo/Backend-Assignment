from django.urls import path
from .views import CarApiOverview, addCars, fetchCars, updateCars, deleteCar

urlpatterns = [
    path('', CarApiOverview),
    path('addCar/', addCars),
    path('fetchCars/', fetchCars),
    path('updateCars/<int:pk>/', updateCars),
    path('deleteCar/<int:pk>/', deleteCar),
]