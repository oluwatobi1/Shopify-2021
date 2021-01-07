"""shopify URL Configuration



"""
from django.urls import path
from .views import ShopFormView, ShopGalleryView


urlpatterns = [
    path('', ShopFormView.as_view()),
    path('gallery', ShopGalleryView.as_view(), name='gallery')
]
