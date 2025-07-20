import django_filters
from .models import Movie, Actor

class MovieFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name='genres__name', lookup_expr='iexact')
    actor = django_filters.CharFilter(field_name='actors__name', lookup_expr='iexact')
    director = django_filters.CharFilter(field_name='director__name', lookup_expr='iexact')
    release_year = django_filters.NumberFilter(field_name='release_year')

    class Meta:
        model = Movie
        fields = ['genre', 'actor', 'director', 'release_year']
        distinct = True

