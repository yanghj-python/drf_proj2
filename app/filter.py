from django_filters.rest_framework import FilterSet

from app.models import Clothes


class LimitFilter:

    def filter_queryset(self, request, queryset, view):
        limit = request.query_params.get("limit")
        if limit and queryset:
            limit = int(limit)
            return queryset[:limit]

        return queryset


# django-filter过滤器类
class ClothesFilterSet(FilterSet):
    from django_filters import filters
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Clothes
        fields = ["brand", "min_price", "max_price"]
