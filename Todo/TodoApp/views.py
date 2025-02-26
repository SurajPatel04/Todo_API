from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(["GET"])
def test_view(request):
    return Response("You requested")


