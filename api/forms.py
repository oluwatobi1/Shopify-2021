from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Shop
from django.contrib.auth.models import User


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ["photo", "name", "description", "price", "tags"]


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=30, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = "__all__"
