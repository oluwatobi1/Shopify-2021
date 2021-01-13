"""shopify URL Configuration



"""

from django.urls import path, include
from .views import ShopFormView, ShopGalleryView, SignUpFormView, LoginView, logout_view

urlpatterns = [
    path('', ShopFormView.as_view(), name='upload_url'),
    path('gallery', ShopGalleryView.as_view(), name='central_gallery_url'),
    path('my_gallery', ShopGalleryView.as_view(), name='personal_gallery_url'),
    path('signup', SignUpFormView.as_view(), name='signup_url'),
    path('login', LoginView.as_view(), name='login_url'),
    path('logout', logout_view, name="logout_url"),

]
