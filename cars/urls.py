from django.urls import path
from .views import test_view, CarApiOverview

urlpatterns = [
    path('hello/', test_view),
    path('overview/', CarApiOverview)
]