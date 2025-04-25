from django.db import models

# Create your models here.
from django.conf import settings # Add this line to the the bottom of the imports 

class Media(models.Model):
    title = models.CharField(max_length=250)
    released = models.DateField(auto_now=False, auto_now_add=False)
    certificate = models.CharField(max_length=3)
    duration = models.DurationField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=250)
    star1 = models.CharField(max_length=250)
    star2 = models.CharField(max_length=250)
    star3 = models.CharField(max_length=250)
    star4 = models.CharField(max_length=250)
    overview = models.TextField(max_length=1000)
    poster = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Rating(models.Model):
    film = models.ForeignKey(Media, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.film} - {self.user}"