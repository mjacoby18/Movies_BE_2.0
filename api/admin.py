from django.contrib import admin
from .models import Movie

class MovieList(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'rating', 'director')
    list_filter = ('name', 'year', 'rating', 'director')
    search_fields = ('name', 'description', 'rating', 'director')
    ordering = ['year']


admin.site.register(Movie, MovieList)
