from django.http import HttpResponseRedirect


def shop_redirect(request):
    return HttpResponseRedirect("shop/")
