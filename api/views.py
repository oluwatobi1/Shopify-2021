from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import ShopForm
from .models import Shop

# Create your views here.


class ShopView(View):
    form_class = ShopForm
    template_name = "api/index.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = {'form':form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        else:
            print(form.errors)
            return HttpResponse("Form Error")

        return render(request, self.template_name, {'form': form})


