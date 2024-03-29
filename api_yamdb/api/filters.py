from reviews.models import Title
import django_filters as filters


class TitleFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name='name', lookup_expr='contains'
    )
    category = filters.CharFilter(
        field_name='category__slug'
    )
    genre = filters.CharFilter(
        field_name='genre__slug'
    )

    class Meta:
        model = Title
        fields = ['name', 'category', 'genre', 'year']
