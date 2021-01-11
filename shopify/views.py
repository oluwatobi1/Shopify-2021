from django.http import HttpResponseRedirect


def shop_redirect(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("shop")
    else:
        return HttpResponseRedirect("shop/login")

