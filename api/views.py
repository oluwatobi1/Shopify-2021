from django.shortcuts import render, HttpResponse
from .models import Shop
from django.views import View

# Create your views here.


class ShopView(View):

    def get(self, request):
        return render(request, "api/index.html")

