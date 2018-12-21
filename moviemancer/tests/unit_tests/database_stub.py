from moviemancer.models import *

class DatabaseStub():
    def create_database_stub():
        Viwer.objects.create(user_id=1, name="hermoione", email="batata@batatinha.com")
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
        Movie.objects.create(movie_id=3, tmdb_movie_id=344, tmdb_title="Blade Runner", tmdb_rating=7, year=1983, runtime=120)
        Movie.objects.create(movie_id=4, tmdb_movie_id=77, tmdb_title="Mean Girls", tmdb_rating=5, year=2004, runtime=120)
        Movie.objects.create(movie_id=5, tmdb_movie_id=55, tmdb_title="Amores Brutos", tmdb_rating=3, year=1980, runtime=80, tmdb_poster='http://image.tmdb.org/t/p/original')

        MovieList.objects.create(movie_list_id=1, movie_id=1, list_id=1)

        Rate.objects.create(rate_id=1, rate=1)
        Rate.objects.create(rate_id=2, rate=2)
        Rate.objects.create(rate_id=3, rate=3)
        Rate.objects.create(rate_id=4, rate=4)
        Rate.objects.create(rate_id=5, rate=5)

        Rating.objects.create(rating_id=1, user_id=1, movie_id=3, rate_id=4)
        Rating.objects.create(rating_id=2, user_id=1, movie_id=4, rate_id=3)

        MovieList.objects.create(movie_list_id=2, movie_id=3, list_id=3)
        MovieList.objects.create(movie_list_id=3, movie_id=4, list_id=3)

        MovieList.objects.create(movie_list_id=4, movie_id=1, list_id=2)