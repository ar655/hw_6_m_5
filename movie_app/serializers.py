from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *

class DirectorListSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = 'id name movies_count movies '.split()

    def get_movies_count(self,obj_director):
        return obj_director.movies.count()

    def get_movies(self,obj_director):
        return [director.title for director in obj_director.movies.all()]


class DirectorBaseValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    def validate_name(self,name):
        if Director.objects.filter(name=name):
            raise ValidationError('name must be unique')
        return name

class DirectorUpdateSerializer( DirectorBaseValidateSerializer):
    pass



class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text  movie'.split()

class ReviewBaseValidateSerializer(serializers.Serializer):
    stars = serializers.IntegerField(default=1)
    text = serializers.CharField(required=False)
    movie = serializers.CharField(max_length=100)
   
class ReviewUpdateSerializer(ReviewBaseValidateSerializer):
    pass





class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()

class MovieBaseValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False)
    duration = serializers.CharField(max_length=10)
    def validate_title(self,title):
        if Movie.objects.filter(title=title):
            raise ValidationError('title must unique')
        return title
class MovieUpdateSerializer(MovieBaseValidateSerializer):
    pass







class MoviesReviewsListSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = ' title  '.split()

    # def get_reviews(self,obj_movie):
    #     return [review.text for review in obj_movie.reviews.all()]
    #
    # def get_rating(self, obj_movie):
    #     for rate in obj_movie.rating.all():
    #         average = sum(rate.rating) / len(rate.rating)
    #         return round(average, 2)
