from django.urls import path
from .views import test_view, CarApiOverview, addCars, fetchCars, updateCars, deleteCar

urlpatterns = [
    path('hello/', test_view),
    path('', CarApiOverview),
    path('addCar/', addCars),
    path('fetchCars/', fetchCars),
    path('updateCars/<int:pk>/', updateCars),
    path('deleteCar/<int:pk>/', deleteCar),
]