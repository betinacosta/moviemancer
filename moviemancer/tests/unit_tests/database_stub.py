from moviemancer.models import *

class DatabaseStub():
    def create_database_stub():
        Viwer.objects.create(user_id=1, name="hermoione")
        Viwer.objects.create(user_id=2, name="luna")

        Type.objects.create(type_id=1, type_name="recommendation")
        Type.objects.create(type_id=2, type_name="watchlist")
        Type.objects.create(type_id=3, type_name="watchedlist")

        List.objects.create(list_id=1, user_id=1, type_id=1)
        List.objects.create(list_id=2, user_id=1, type_id=2)
        List.objects.create(list_id=3, user_id=1, type_id=3)

        List.objects.create(list_id=4, user_id=2, type_id=1)
        List.objects.create(list_id=5, user_id=2, type_id=2)
        List.objects.create(list_id=6, user_id=2, type_id=3)

        Movie.objects.create(movie_id=1, tmdb_movie_id=533, tmdb_title="Princess Bride", tmdb_rating=6, year=1998, runtime=93)
        Movie.objects.create(movie_id=2, tmdb_movie_id=123, tmdb_title="Monty Python", tmdb_rating=9, year=1974, runtime=120)

        MovieList.objects.create(movie_list_id=1, movie_id=1, list_id=1)