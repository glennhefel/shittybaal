from django.contrib import admin

# Register your models here.

from . models import Media, Rating

admin.site.register(Media)
admin.site.register(Rating)