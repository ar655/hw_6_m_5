from rest_framework.decorators import api_view
from rest_framework.response import Response

from.serializers import *
from.models import *
from rest_framework import status

@api_view(['GET','POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorListSerializer(directors,many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(
            name=name
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
        name = request.data.get('name')
        director.name = name
        director.save()
        return Response(data=DirectorListSerializer(director).data)



@api_view(['GET','POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewListSerializer(reviews,many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        review = Review.objects.create(
            text=text
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
        text = request.data.get('text')
        review.text = text
        return Response(data=ReviewListSerializer(review).data)



@api_view(['GET','POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieListSerializer(movies,many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration
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