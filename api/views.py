from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import ListView
from django.utils import timezone

from .forms import ShopForm
from .models import Shop

# Create your views here.


class ShopFormView(View):
    form_class = ShopForm
    template_name = "api/index.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = {'form':form}
        return render(request, self.template_name, context)

    # TODO refactor form post
    # TODO work/Add on form Validations.
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form['uploaded_by'] = self.user.username
            print(self.user.username, "usererrer")

            # form.save()
            return HttpResponseRedirect('/shop/gallery')
        else:
            print(form.errors)
            return HttpResponse("Form Error")
        return render(request, self.template_name, {'form': form})


class ShopGalleryView(ListView):
    model = Shop
    # TODO work on pagination
    # paginate_by = 2
    template_name = "api/Gallery.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['now'] = timezone.now()
        return context






