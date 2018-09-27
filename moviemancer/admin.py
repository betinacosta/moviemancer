from django.contrib import admin

#Database import

from .models import List, Movie, MovieList, Rate, Rating, Type, Viwer

admin.site.register(List)
admin.site.register(Movie)
admin.site.register(MovieList)
admin.site.register(Rate)
admin.site.register(Rating)
admin.site.register(Type)
admin.site.register(Viwer)