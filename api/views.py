from django.shortcuts import render, HttpResponse
from .models import Shop

# Create your views here.


def view(request):
    return HttpResponse("Here")
