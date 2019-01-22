from django.test import TestCase
from moviemancer.queries import *
from moviemancer.models import *
from unittest import mock

class DatabaseTestCase(TestCase):

    def setUp(self):
        Movie.objects.create(tmdb_movie_id=3, tmdb_title="Princess Bride", tmdb_rating=6, year=1998, runtime=93)

        Viwer.objects.create(name="luna")
        Viwer.objects.create(user_id=88, name='test', email='bla@test', password='secure')

        Type.objects.create(type_id=1, type_name="recommendation")
        Type.objects.create(type_id=3, type_name="watchedlist")

        List.objects.create(list_id=11, user_id=1, type_id=1)
        List.objects.create(list_id=22, user_id=1, type_id=2)
        List.objects.create(list_id=33, user_id=1, type_id=3)

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
        MovieList.objects.create(movie_id=1, list_id=33)
        remove_movie_from_list(user_id=1, movie_id=1, list_type=3)

        self.assertFalse(MovieList.objects.filter(movie_id=1, list_id=33))

    def test_should_remove_user_rating_to_given_movie(self):
        Rating.objects.create(user_id=1, movie_id=1, rate_id=4)
        remove_rating(user_id=1, movie_id=1)

        self.assertFalse(Rating.objects.filter(user_id=1, movie_id=1))

    def test_should_remove_movie_from_watched_list(self):
        MovieList.objects.create(movie_id=2, list_id=33)
        Rating.objects.create(user_id=1, movie_id=2, rate_id=4)
        remove_watched(user_id=1, movie_id=2, list_type=3)

        self.assertFalse(Rating.objects.filter(user_id=1, movie_id=2))
        self.assertFalse(MovieList.objects.filter(movie_id=2, list_id=33))

    def test_should_create_movie_and_add_to_list(self):
        add_to_list_external(user_id=1, tmdb_movie_id=22, tmdb_poster="htttp://bla.jpg", tmdb_title="Batatas Furiosas", list_type=3)

        movie_queryset = Movie.objects.filter(tmdb_movie_id=22)
        self.assertTrue(movie_queryset)

        self.assertTrue(MovieList.objects.filter(movie_id=movie_queryset[0].movie_id, list_id=33))

    def test_should_add_existent_movie_to_list(self):
        Movie.objects.create(movie_id=99, tmdb_movie_id=533, tmdb_title="Batatas Furiosas", tmdb_rating=6, year=1998, runtime=93)
        add_to_list_external(user_id=1, tmdb_movie_id=533, tmdb_poster="htttp://bla.jpg", tmdb_title="Batatas Furiosas", list_type=3)

        self.assertTrue(MovieList.objects.filter(movie_id=99, list_id=33))
        self.assertTrue(len(Movie.objects.filter(tmdb_movie_id=533)) == 1)

    def test_should_add_movie_to_list(self):
        Movie.objects.create(movie_id=66, tmdb_movie_id=7, tmdb_title="Furiosas Batatas", tmdb_rating=6, year=1998, runtime=93)
        add_to_list(user_id=1, movie_id=66, list_type=1)

        self.assertTrue(MovieList.objects.filter(movie_id=66, list_id=11))

    def test_should_remove_from_recomendation_if_added_to_other_list(self):
        add_to_list(user_id=1, movie_id=99, list_type=1)

        self.assertFalse(MovieList.objects.filter(movie_id=99, list_id=33))

    def test_should_add_movie_to_watchedlist_when_rated(self):
        rate_movie(user_id=1, movie_id=33, local_rate_id=5)

        self.assertTrue(MovieList.objects.filter(movie_id=33, list_id=33))

    def test_should_remove_movie_from_watchlist_when_rated(self):
        rate_movie(user_id=1, movie_id=66, local_rate_id=5)

        self.assertFalse(MovieList.objects.filter(movie_id=66, list_id=11))

    def test_should_add_new_movie_to_watchedlist_when_rated(self):
        rate_external_movie(user_id=1, user_rating=3, tmdb_movie_id=99, tmdb_poster='bla.jpg', tmdb_title="The Amazing Papas")
        movie_queryset = Movie.objects.filter(tmdb_movie_id=99)

        self.assertTrue(movie_queryset)
        self.assertTrue(MovieList.objects.filter(movie_id=movie_queryset[0].movie_id, list_id=33))

    @mock.patch('moviemancer.queries.create_list_to_user')
    @mock.patch('moviemancer.queries.create_user')
    @mock.patch('moviemancer.queries.get_user_id')
    def test_should_create_user_and_its_lists(self, mock_create_list_to_user, mock_create_user, mock_get_user_id):
        register_user(name='ana', email='ana@ana', password='123')

        mock_create_list_to_user.assert_called()
        mock_create_user.assert_called()
        mock_get_user_id.assert_called()

    def test_should_return_user_id_when_registered(self):
        self.assertIsNotNone(register_user(name='batata', email='batata@batata', password='456'))

    @mock.patch('moviemancer.models.Viwer.save')
    def test_should_create_user_if_doesent_exists(self, mock_save_viewer):
        create_user(name='mila', email='mila@mila', password='mileumanoites')
        mock_save_viewer.assert_called()

    def test_should_return_none_if_user_already_exists(self):
        Viwer.objects.create(name='test', email='test@test', password='secure')
        self.assertIsNone(create_user(name='test', email='test@test', password='secure'))

    @mock.patch('moviemancer.models.List.save')
    def test_should_create_list_to_user(self, mock_create_list_to_user):
        create_list_to_user(user_id=5, type_id=3)
        mock_create_list_to_user.assert_called()

    def test_should_handle_user_update_info(self):

        user = handle_user_update_info(user_id=88, email=' ', name='new', password=None)
        self.assertEqual(user.user_id, 88)
        self.assertEqual(user.email, 'bla@test')
        self.assertEqual(user.name, 'new')

    @mock.patch('moviemancer.models.Viwer.save')
    def test_should_update_user(self, mock_update_user_info):
        update_user_info(user_id=88, email='new@new', name='new', password='')
        mock_update_user_info.assert_called()

