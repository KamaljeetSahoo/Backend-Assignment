from django.urls import path
from .views import test_view, CarApiOverview, addCars, fetchCars

urlpatterns = [
    path('hello/', test_view),
    path('', CarApiOverview),
    path('addCar/', addCars),
    path('fetchCars/', fetchCars),
]