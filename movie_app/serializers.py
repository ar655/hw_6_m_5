from rest_framework import serializers

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



class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text  movie'.split()


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()




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
