from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ShopForm, SignUpForm
from .models import Shop



# Create your views here.


class ShopFormView(LoginRequiredMixin, View):
    form_class = ShopForm
    template_name = "api/image_upload.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = {'form': form}
        return render(request, self.template_name, context)

    # TODO refactor form post
    # TODO work/Add on form Validations (done for sign/login).
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        form.instance.uploaded_by = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/shop/my_gallery')
        return render(request, self.template_name, {'form': form})


class ShopCentralGalleryView(LoginRequiredMixin, ListView):
    model = Shop
    # TODO work on pagination
    # paginate_by = 2
    template_name = "api/central_gallery.html"

    # search functionality
    def get_queryset(self):
        search_text = self.request.GET.get('tags')
        if search_text:
            items = Shop.objects.filter(Q(tags__icontains=search_text) |
                                       Q(description__icontains=search_text))
            if items:
                return items
            else:
                return "Not found"
        else:
            return Shop.objects.all()


class ShopPersonalGalleryView(LoginRequiredMixin, ListView):
    model = Shop
    # TODO work on pagination
    # paginate_by = 2
    template_name = "api/personal_gallery.html"

    # search functionality
    def get_queryset(self):
        print(self.request.user)
        search_text = self.request.GET.get('tags')
        if search_text:
            items = Shop.objects.filter((Q(tags__icontains=search_text) |
                                       Q(description__icontains=search_text)) &
                                       Q(uploaded_by__iexact=self.request.user.username))
            if items:
                return items
            else:
                return "Not found"
        else:
            return Shop.objects.filter(uploaded_by__exact=self.request.user)


class SignUpFormView(View):
    form_class = SignUpForm
    template_name = "api/signup_form.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = {'signup_form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # TODo this form.save check it
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/shop/gallery')
        else:
            print(form.errors)
            context = {'signup_form': form}
            return render(request, self.template_name, context=context)


class LoginView(View):
    template_name = "api/login_form.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/shop/gallery')
        else:
            return render(request, self.template_name, {'message': 'Invalid Login Credentials'})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/shop/login')


class ShopGalleryDetailView(DetailView):
    model = Shop
    template_name = "api/gallery_detail.html"

