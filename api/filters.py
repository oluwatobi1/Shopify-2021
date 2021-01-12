import django_filters

from api.models import Shop


class ShopTextFilter(django_filters.FilterSet):
    class Meta:
        model = Shop
        fields = ['tags', "description"]
