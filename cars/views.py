from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serlializers import CarSerializer

# Create your views here.
def test_view(request):
    return HttpResponse("<h1>Hello</h1>")

@api_view(['GET'])
def CarApiOverview(request):
    api_urls = {
        'all_items' : '/'
    }
    return Response(api_urls)