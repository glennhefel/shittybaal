from django.shortcuts import render, get_object_or_404

# Create your views here.
from . models import Media, Rating

def homepage(request):
    media = Media.objects.all()

    context = {"media":media}
    return render(request, "media/homepage.html", context)

def media_detail(request, pk):  
    media = get_object_or_404(Media, pk=pk)
    context = {"media": media}
    return render(request, "media/m_details.html", context)


    

    
