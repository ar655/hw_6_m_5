from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from.serializers import *
from.models import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     )
from rest_framework.pagination import PageNumberPagination


from rest_framework.viewsets import ModelViewSet


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorListSerializer


class DirectorUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorListSerializer
    lookup_field = 'id'


class ReviewlistAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer


class ReviewUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    lookup_field = 'id'


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

class MovieUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    lookup_field = 'id '


@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorListSerializer(directors,many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = DirectorBaseValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'message': 'data with errors',
                                  'error': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        director = Director.objects.create(
            name=request.data.get('name')
        )
        return Response(data=DirectorListSerializer(director).data)


@api_view(['GET', 'PUT', 'DELETE'])
def get_one_director_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'ERROR': 'Director not found'})
    if request.method == 'GET':
        data = DirectorListSerializer(director).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = DirectorUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = request.data.get('name')
        director.name = name
        director.save()
        return Response(data=DirectorListSerializer(director).data)



@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewListSerializer(reviews,many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer =ReviewBaseValidateSerializer (data=request.data)
        if not serializer.is_valid():
            return Response(data={'message': 'data with errors',
                                  'error': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        review = Review.objects.create(
            text=request.data.get('text'),
            movie=request.data.get('movie')
        )
        return Response(data=ReviewListSerializer(review).data)



@api_view(['GET','PUT','DELETE'])
def get_one_review_view(request,id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data={'ERROR':'Review not found'})
    if request.method == 'GET':
        data = ReviewListSerializer(review).data
        return Response(data=data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        review.text = text
        review.movie = movie
        review.stars = stars
        return Response(data=ReviewListSerializer(review).data)



@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieListSerializer(movies,many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = MovieBaseValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'message': 'data with errors',
                                  'error': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        movie = Movie.objects.create(
            title=request.data.get('title'),
            description=request.data.get('description'),
            duration=request.data.get('duration')
        )
        return Response(data=MovieListSerializer(movie).data)


@api_view(['GET','PUT','DELETE'])
def get_one_movie_view(request,id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data={'ERROR':'Movie not found'})
    if request.method == 'GET':
        data = MovieListSerializer(movie).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MovieUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        movie.title = title
        movie.description = description
        movie.duration = duration
        movie.save()
        return Response(data=MovieListSerializer(movie).data)




@api_view(['GET'])
def get_one_movie_review_view(request,id):
    try:
       movie_review = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data={'ERROR':'Movie not found'})
    return Response(data=MoviesReviewsListSerializer(movie_review).data)