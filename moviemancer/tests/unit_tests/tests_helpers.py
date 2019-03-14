from django.test import TestCase
from moviemancer.helpers import Helpers
from moviemancer.tests.unit_tests.database_stub import DatabaseStub
from moviemancer.models import *

class HelpersTestCase(TestCase):
    def setUp(self):
        DatabaseStub.create_database_stub()

    def test_should_return_list_by_user(self):
        self.assertEqual(Helpers.get_user_list_id_by_type_id(user_id=1, type_id=3), 3)

    def test_should_return_list_by_user_based_on_list_name(self):
        self.assertEqual(Helpers.get_user_list_id_by_type_name(user_id=1, list_type="recommendation"), 1)

    def test_should_convert_tmdb_rating_to_five(self):
        self.assertEqual(Helpers.convert_tmdb_rating(9),5)

    def test_should_convert_tmdb_rating_to_four(self):
        self.assertEqual(Helpers.convert_tmdb_rating(8.8),4)

    def test_should_format_date_to_year_only(self):
        self.assertEqual(Helpers.formate_date_to_year('2000-06-16'), '2000')

    def test_should_return_genres_separeted_by_comas(self):
        genres='18,53'
        entry = [{'id': 18, 'name': 'Drama'}, {'id': 53, 'name': 'Thriller'}]
        self.assertEqual(Helpers.get_comma_separeted_genres(genre_list = entry), genres)

    def test_should_return_true_if_movie_on_user_list(self):
        self.assertTrue(Helpers.is_movie_on_list(user_id=1, movie_id=1, type_id=1))

    def test_should_return_false_if_movie_not_on_user_list(self):
        self.assertFalse(Helpers.is_movie_on_list(user_id=2, movie_id=1, type_id=2))

    def test_should_return_movie_raw_in_a_list_by_user(self):
        movie = Movie(movie_id=1, tmdb_movie_id=533, tmdb_title="Princess Bride", tmdb_rating=6, year=1998, runtime=93)

        self.assertEqual(Helpers.movie_by_user_list(1, "recommendation")[0], movie)

    def test_should_return_movie_object_in_a_list_by_user(self):
        movie_list = MovieList(movie_list_id=1, movie_id=1, list_id=1)

        self.assertEqual(list(Helpers.movie_id_by_user_list(user_id=1,type_id=1)), [movie_list])

    def test_should_return_rated_movies_by_user(self):
        self.assertEqual(Helpers.get_rated_movies_by_user(1), {3: 4, 4: 3})

    def test_should_return_user_rate_to_movie(self):
        self.assertEqual(Helpers.get_user_rate_to_movie(3, 1), 4)

    def test_should_return_user_id_by_email(self):
        self.assertEqual(Helpers.get_user_id_by_email("batata@batatinha.com"), 1)

    def test_should_return_tmdb_id_by_movie_id(self):
        self.assertEqual(Helpers.get_tmdb_id_by_movie_id(1), 533)

    def test_should_return_movie_id_by_tmdb_id(self):
        self.assertEqual(Helpers.get_movie_id_by_tmdb_id(533), 1)

    def test_should_return_movie_title_by_movie_id(self):
        self.assertEqual(Helpers.get_movie_title_internal(movie_id=1), "Princess Bride")

    def test_should_return_link_to_movie_poster_by_movie_id(self):
        self.assertIn('http://image.tmdb.org/t/p/original', Helpers.get_movie_poster_internal(5))

    def test_should_return_watchedlist_for_a_user(self):
        movie_list = [
            {'movie_id': 3, 'poster': '', 'rating': 4, 'title': 'Blade Runner', 'tmdb_movie_id': 344},
            {'movie_id': 4, 'poster': '', 'rating': 3, 'title': 'Mean Girls', 'tmdb_movie_id': 77}
        ]
        self.assertEqual(Helpers.get_watchedlist(1), movie_list)

    def test_should_return_tmdb_rating_by_movie_id(self):
        self.assertEqual(Helpers.get_tmdb_rating_internal(1), 6)

    def test_should_return_watchlist_for_a_user(self):
        movie_list = [
            {'movie_id': 1, 'poster': '', 'title': 'Princess Bride', 'tmdb_movie_id': 533, 'tmdb_rating': 6}
        ]
        self.assertEqual(Helpers.get_watchlist(1), movie_list)

    def test_should_return_recommendation_list_for_a_user(self):
        movie_list = [
            {'movie_id': 1, 'tmdb_movie_id': 533, 'tmdb_poster': '', 'tmdb_rating': 6, 'tmdb_title': 'Princess Bride'}
        ]
        self.assertEqual(Helpers.get_recommendation_list(1, 3), movie_list)

    def test_should_return_true_for_registered_user(self):
        self.assertTrue(Helpers.user_exists("batata@batatinha.com"))

    def test_should_return_false_for_registered_user(self):
        self.assertFalse(Helpers.user_exists("nope@nope.com"))

    def test_should_return_user_id(self):
        self.assertEqual(Helpers.get_user_id(email="batata@batatinha.com"), 1)

    def test_should_handle_user_update_info(self):
        Viwer.objects.create(user_id=45, name='test', email='bla@test', password='secure')

        user = Helpers.handle_user_update_info(user_id=45, email=' ', name='new', password=None)
        self.assertEqual(user.user_id, 45)
        self.assertEqual(user.email, 'bla@test')
        self.assertEqual(user.name, 'new')

    def test_should_return_user_information(self):
        Viwer.objects.create(user_id=99, name="A User", email='auser@user')

        user = {'email': 'auser@user', 'name': 'A User', 'user_id': 99}
        self.assertEqual(Helpers.get_user(email='auser@user'), user)

    def test_should_return_comments_based_on_tmdb_movie_id(self):
        Movie.objects.create(movie_id=99, tmdb_movie_id=8, tmdb_title="test", tmdb_rating=6, year=1998, runtime=93)
        Viwer.objects.create(user_id=77, name='pria', email='pria@mail')
        Comments.objects.create(user_id=77, movie_id=99, comment='muito bom, 2 estrelas')

        comment = [{'comment_id': 1, 'user_name': 'pria', 'comment': 'muito bom, 2 estrelas', 'rate': 0}]

        self.assertEqual(Helpers.get_comments(movie_tmdb_id=8), comment)

    def test_should_return_all_rated_movies(self):
        rated_movies=[{'movie_id': 3, 'title': 'Blade Runner', 'poster': ''}, {'movie_id': 4, 'title': 'Mean Girls', 'poster': ''}]

        self.assertEqual(Helpers.get_rated_movies(), rated_movies)

    def test_should_return_better_rated_movies_according_to_trashold(self):
        better_rated=[3, 4]
        self.assertEqual(Helpers.get_best_ratted_movies_by_user(user_id=1, trashold=3), better_rated)

    def test_should_return_true_for_existent_movie(self):
        self.assertTrue(Helpers.is_movie_on_database(tmdb_movie_id=533))

    def test_should_return_false_for_non_existent_movie(self):
        self.assertFalse(Helpers.is_movie_on_database(tmdb_movie_id=989898))


