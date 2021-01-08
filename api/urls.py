"""shopify URL Configuration



"""
from django.urls import path
from .views import ShopFormView, ShopGalleryView


urlpatterns = [
    path('', ShopFormView.as_view(), name='upload'),
    path('gallery', ShopGalleryView.as_view(), name='gallery')
]
