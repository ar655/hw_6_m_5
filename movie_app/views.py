from rest_framework.decorators import api_view
from rest_framework.response import Response

from.serializers import *
from.models import *
from rest_framework import status

@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    data = DirectorListSerializer(directors,many=True).data
    return Response(data=data)

@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    data = ReviewListSerializer(reviews,many=True).data
    return Response(data=data)


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    data = MovieListSerializer(movies,many=True).data
    return Response(data=data)

@api_view(['GET'])
def get_one_director_view(request,id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data={'ERROR':'Director not found'})
    return Response(data=DirectorListSerializer(director).data)

@api_view(['GET'])
def get_one_movie_view(request,id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data={'ERROR':'Movie not found'})
    return Response(data=MovieListSerializer(movie).data)



@api_view(['GET'])
def get_one_review_view(request,id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data={'ERROR':'Review not found'})
    return Response(data=ReviewListSerializer(review).data)


@api_view(['GET'])
def get_one_movie_review_view(request,id):
    try:
       movie_review = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data={'ERROR':'Movie not found'})
    return Response(data=MoviesReviewsListSerializer(movie_review).data)