"""shopify URL Configuration



"""

from django.urls import path, include
from .views import (ShopFormView, ShopCentralGalleryView,
                    SignUpFormView, LoginView, logout_view,
                    ShopPersonalGalleryView, ShopGalleryDetailView, )

urlpatterns = [
    path('', ShopFormView.as_view(), name='upload_url'),
    path('gallery', ShopCentralGalleryView.as_view(), name='central_gallery_url'),
    path('my_gallery', ShopPersonalGalleryView.as_view(), name='personal_gallery_url'),
    path('signup', SignUpFormView.as_view(), name='signup_url'),
    path('login', LoginView.as_view(), name='login_url'),
    path('logout', logout_view, name="logout_url"),
    path('gallery/<int:pk>/', ShopGalleryDetailView.as_view(), name='gallery_detail_url')

]
