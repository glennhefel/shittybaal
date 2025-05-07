from django.contrib import admin

# Register your models here.

from . models import Media, Rating
from .models import Hanekawa #Kuro

admin.site.register(Media)
admin.site.register(Rating)

@admin.register(Hanekawa)
class HanekawaAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'vote_type')