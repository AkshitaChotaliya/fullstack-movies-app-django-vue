from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Movie, Actor, Director, Genre
from .serializers import *
from .filters import MovieFilter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .error import error_response



# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().prefetch_related('genres', 'actors').select_related('director')
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('genres__name', openapi.IN_QUERY, description="Genre name", type=openapi.TYPE_STRING),
            openapi.Parameter('director__name', openapi.IN_QUERY, description="Director name", type=openapi.TYPE_STRING),
            openapi.Parameter('release_year', openapi.IN_QUERY, description="Release year", type=openapi.TYPE_INTEGER),
            openapi.Parameter('release_year__gte', openapi.IN_QUERY, description="Release year greater than or equal to", type=openapi.TYPE_INTEGER),

        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MovieCreateUpdateSerializer
        return MovieSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('role', openapi.IN_PATH, description="Role: actor or director", type=openapi.TYPE_STRING),
        openapi.Parameter('id', openapi.IN_PATH, description="Person ID", type=openapi.TYPE_INTEGER),
    ],
    responses={200: openapi.Response("Person profile with movies", MovieShortSerializer(many=True))}
)

@api_view(['GET'])
def person_detail(request, role, id):
    if role == 'actor':
        person = get_object_or_404(Actor, pk=id)
        movies = person.movies.all()
    elif role == 'director':
        person = get_object_or_404(Director, pk=id)
        movies = person.directed_movies.all()
    else:
        return Response({"error": "Invalid role"}, status=400)

    return Response({
        "name": person.name,
        "movies": MovieShortSerializer(movies, many=True).data
    })
