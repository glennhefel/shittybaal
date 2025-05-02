from random import randint  

from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Avg
from .models import Media, Rating
import os, json
from datetime import timedelta
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
# Create your views here.


module_dir = os.path.dirname(__file__) # get current directory

# def add_media(request):
#     file_path = os.path.join(module_dir, 'top.json') 
#     with open(file_path, 'r', encoding='utf-8') as f: 
#         data = json.load(f)
    
#     no_added = 0
#     for media in data:
#         dur = media['Runtime']
#         obj = Media.objects.update_or_create(
#             title=data["Series_Title"],
#             released=data['Released_Year'],
#             #media=data['media'],
#             genre=data['Genre'],
#             director=data['Director'],
#             poster=data['Poster_Link']
#         )
#         no_added += 1

#     messsage = f"Added {no_added} to your database"
#     return HttpResponse(messsage, content_type="text/plain")


def homepage(request):
    media = Media.objects.all()
    context = {"media":media}
    return render(request, "media/homepage.html", context)


def media_detail(request, pk):  
    media = get_object_or_404(Media, pk=pk)
    context = {"media": media}
    return render(request, "media/m_details.html", context)


def add_reviews(request):
    for j in range(0,10000):
        for i in range(1,5):
            mediaID = randint(1,500)
            mediaRating = randint(1,10)
            add_rev(mediaID, i, mediaRating)
    return redirect("films:homepage")


def add_rev(g_media, g_user, g_rating):
    obj, create = Rating.objects.get_or_create(
        media = get_object_or_404(Media, pk=g_media),
        user = get_object_or_404(User, pk=g_user),
        rating = g_rating,
    )

    
# def top250(request):
#     films = Film.objects.annotate(avr=Avg("ratings__rating"), votes=Count("ratings__rating")).order_by("-avr")[0:250]
#     paginator = Paginator(films, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {"films":films, "page_obj":page_obj}
#     return render(request, "films/homepage.html", context)

# def most_votes(request):
#     films = Film.objects.annotate(avr=Avg("ratings__rating"), votes=Count("ratings__rating")).order_by("-votes")[0:250]
#     paginator = Paginator(films, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {"films":films, "page_obj":page_obj}
#     return render(request, "films/homepage.html", context)

# def bot250(request):
#     films = Film.objects.annotate(avr=Avg("ratings__rating")).order_by("avr")[0:250]
#     paginator = Paginator(films, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {"films":films, "page_obj":page_obj}
#     return render(request, "films/homepage.html", context)

# def add_films(request):
#     file_path = os.path.join(module_dir, 'imdb_top_films.json')
#     with open(file_path, "r", encoding="utf-8") as f:
#         data = json.load(f)
#     no_added = 0
#     for film in data:
#         dur = film["Runtime"]
#         f_dur = timedelta(minutes=int(dur[0:-4]))
#         obj = Film.objects.update_or_create(
#             title = film[y],
#             released = f"{film['Released_Year']}-01-01",
#             certificate = film["Certificate"],
#             duration = f_dur,
#             genre = film["Genre"],
#             director = film["Director"],
#             star1 = film["Star1"],
#             star2 = film["Star2"],
#             star3 = film["Star3"],
#             star4 = film["Star4"],
#             overview = film["Overview"],
#             poster = film["Poster_Link"]
#         )
#         no_added += 1
#     msg = f"Added {no_added} films to the database."
#     return HttpResponse(msg, content_type="text/plain")
    
