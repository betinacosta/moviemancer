from django.contrib import admin

#Database import

from .models import Cast, Genre, List, Movie, MovieList, Profile, ProfileCast, ProfileGenre, Rate, Rating, Type, User

admin.site.register(Cast)
admin.site.register(Genre)
admin.site.register(List)
admin.site.register(Movie)
admin.site.register(MovieList)
admin.site.register(Profile)
admin.site.register(ProfileCast)
admin.site.register(ProfileGenre)
admin.site.register(Rate)
admin.site.register(Rating)
admin.site.register(Type)
admin.site.register(User)

