from django.test import TestCase
from moviemancer.queries import *
from moviemancer.models import *

class DatabaseTestCase(TestCase):

    def setUp(self):
        Movie.objects.create(tmdb_movie_id=3, tmdb_title="Princess Bride", tmdb_rating=6, year=1998, runtime=93)

        Viwer.objects.create(name="luna")

        Type.objects.create(type_id=1, type_name="recommendation")
        Type.objects.create(type_id=3, type_name="watchedlist")

        List.objects.create(list_id=1, user_id=1, type_id=1)
        List.objects.create(list_id=2, user_id=1, type_id=2)
        List.objects.create(list_id=3, user_id=1, type_id=3)

    def test_should_add_new_movie_to_database(self):
        self.assertEqual(add_movie_to_database(543), 'Success')

    def test_should_return_error_if_movie_exists_in_db(self):
        self.assertEqual(add_movie_to_database(3), 'Error: movie already exists')

    def test_should_add_new_rate_to_movie(self):
        add_rating_to_movie(user_id=5, movie_id=44, local_rate_id=3)
        self.assertTrue(Rating.objects.filter(user_id=5, movie_id=44))

    def test_should_update_existing_movie_rate(self):
        add_rating_to_movie(user_id=5, movie_id=55, local_rate_id=3)
        add_rating_to_movie(user_id=5, movie_id=55, local_rate_id=5)

        self.assertTrue(Rating.objects.filter(user_id=5, movie_id=55, rate_id=5))

    def test_should_remove_movie_from_list(self):
        MovieList.objects.create(movie_id=1, list_id=3)
        remove_movie_from_list(user_id=1, movie_id=1, list_type=3)

        self.assertFalse(MovieList.objects.filter(movie_id=1, list_id=3))

    def test_should_remove_user_rating_to_given_movie(self):
        Rating.objects.create(user_id=1, movie_id=1, rate_id=4)
        remove_rating(user_id=1, movie_id=1)

        self.assertFalse(Rating.objects.filter(user_id=1, movie_id=1))

    def test_should_remove_movie_from_watched_list(self):
        MovieList.objects.create(movie_id=2, list_id=3)
        Rating.objects.create(user_id=1, movie_id=2, rate_id=4)
        remove_watched(user_id=1, movie_id=2, list_type=3)

        self.assertFalse(Rating.objects.filter(user_id=1, movie_id=2))
        self.assertFalse(MovieList.objects.filter(movie_id=2, list_id=3))

    def test_should_create_movie_and_add_to_list(self):
        add_to_list_external(user_id=1, tmdb_movie_id=22, tmdb_poster="htttp://bla.jpg", tmdb_title="Batatas Furiosas", list_type=3)

        movie_queryset = Movie.objects.filter(tmdb_movie_id=22)
        self.assertTrue(movie_queryset)

        self.assertTrue(MovieList.objects.filter(movie_id=movie_queryset[0].movie_id, list_id=3))

    def test_should_add_existent_movie_to_list(self):
        Movie.objects.create(movie_id=99, tmdb_movie_id=533, tmdb_title="Batatas Furiosas", tmdb_rating=6, year=1998, runtime=93)
        add_to_list_external(user_id=1, tmdb_movie_id=533, tmdb_poster="htttp://bla.jpg", tmdb_title="Batatas Furiosas", list_type=3)

        self.assertTrue(MovieList.objects.filter(movie_id=99, list_id=3))
        self.assertTrue(len(Movie.objects.filter(tmdb_movie_id=533)) == 1)

    def test_should_add_movie_to_list(self):
        Movie.objects.create(movie_id=66, tmdb_movie_id=7, tmdb_title="Furiosas Batatas", tmdb_rating=6, year=1998, runtime=93)
        add_to_list(user_id=1, movie_id=66, list_type=1)

        self.assertTrue(MovieList.objects.filter(movie_id=66, list_id=1))

    def test_should_remove_from_recomendation_if_added_to_other_list(self):
        add_to_list(user_id=1, movie_id=99, list_type=1)

        self.assertFalse(MovieList.objects.filter(movie_id=99, list_id=3))

    def test_should_add_movie_to_watchedlist_when_rated(self):
        rate_movie(user_id=1, movie_id=33, local_rate_id=5)

        self.assertTrue(MovieList.objects.filter(movie_id=33, list_id=3))

    def test_should_remove_movie_from_watchlist_when_rated(self):
        rate_movie(user_id=1, movie_id=66, local_rate_id=5)

        self.assertFalse(MovieList.objects.filter(movie_id=66, list_id=1))
