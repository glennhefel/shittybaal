from django.db import models

# Create your models here.
from django.conf import settings # Add this line to the the bottom of the imports 

media_li=[
    ("Anime", "Anime"),
    ("Movies", "Movies"),
    ("TV_series", "TV_series")
]

genre_li=[
    ("action","action"),
    #("psychological","psychological"), ("comedy","comedy"), ("romance","romance"), ("sci-fi cyberpunk","sci-fi cyberpunk"), 


]

class Media(models.Model):
    title = models.CharField(max_length=250)
    released = models.DateField(auto_now=False, auto_now_add=False)
    media = models.CharField(max_length=10 , choices=media_li)
    #certificate = models.CharField(max_length=3)
    #duration = models.DurationField()
    genre = models.CharField(max_length=30, choices=genre_li)
    director = models.CharField(max_length=250)
    #star1 = models.CharField(max_length=250)
    #star2 = models.CharField(max_length=250)
    #star3 = models.CharField(max_length=250)
    #star4 = models.CharField(max_length=250)
    #overview = models.TextField(max_length=1000)
    poster = models.URLField(max_length=500)

    def __str__(self):
        return self.title

class Rating(models.Model):
    film = models.ForeignKey(Media, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.film} - {self.user}"