"""shopify URL Configuration



"""

from django.urls import path
from .views import ShopFormView, ShopGalleryView, SignUpFormView, LoginView

urlpatterns = [
    path('', ShopFormView.as_view(), name='upload_url'),
    path('gallery', ShopGalleryView.as_view(), name='gallery_url'),
    path('signup', SignUpFormView.as_view(), name='signup_url'),
    path('login', LoginView.as_view(), name='login_url'),

]
