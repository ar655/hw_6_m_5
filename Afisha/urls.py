
from django.contrib import admin
from django.urls import path,include
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/',views.directors_view),
    path('api/v1/movies/',views.movies_view),
    path('api/v1/reviews/',views.reviews_view),
    path('api/v1/reviews/<int:id>/',views.get_one_review_view),
    path('api/v1/movies/<int:id>/',views.get_one_movie_view),
    path('api/v1/directors/<int:id>/',views.get_one_director_view),
    path('api/v1/movies/reviews/<int:id>',views.get_one_movie_review_view),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/directors/',views.DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorUpdateDeleteAPIView.as_view()),
    path('api/v1/reviews/',views.ReviewlistAPIView.as_view()),
    path('api/v1/reviews/<int:id>/',views.ReviewUpdateDeleteAPIView.as_view()),
    path('api/v1/movies/',views.MovieListAPIView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieUpdateDeleteAPIView.as_view()),

]
