from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
       return self.name


class Movie(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=10)
    director = models.ForeignKey(
        to=Director,
        null=True,
        related_name='movies',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    @property
    def director_name(self):
        try:
            return self.director.name
        except:
            return 'ERROR'


class Review(models.Model):
    rate = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')
    )
    review = models.ForeignKey(
        to=Movie,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='review'
    )
    stars = models.IntegerField(default=1,choices=rate)
    text = models.TextField(blank=True,null=True)
    movie = models.CharField(max_length=100)


    @property
    def movie_name(self):
        try:
            return self.review.title
        except:
            return 'ERROR'

    def __str__(self):
        return f'{self.movie}-{self.stars}'