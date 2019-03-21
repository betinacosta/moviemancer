from django.test import TestCase
from moviemancer.collaborative_filtering import CollaborativeFiltering
from moviemancer.models import *
from unittest import mock

class CollaborativeFilteringTestCase(TestCase):
    def setUp(self):
        Viwer.objects.create(user_id=1, name="hermoione", email="batata@batatinha.com")
        Viwer.objects.create(user_id=2, name="luna")

        Type.objects.create(type_id=3, type_name="watchedlist")

        List.objects.create(list_id=3, user_id=1, type_id=3)

        List.objects.create(list_id=6, user_id=2, type_id=3)

        Movie.objects.create(movie_id=1, tmdb_movie_id=533, tmdb_title="Princess Bride", tmdb_rating=6, year=1998, runtime=93)
        Movie.objects.create(movie_id=2, tmdb_movie_id=123, tmdb_title="Monty Python", tmdb_rating=9, year=1974, runtime=120)
        Movie.objects.create(movie_id=3, tmdb_movie_id=344, tmdb_title="Blade Runner", tmdb_rating=7, year=1983, runtime=120)
        Movie.objects.create(movie_id=4, tmdb_movie_id=77, tmdb_title="Mean Girls", tmdb_rating=5, year=2004, runtime=120)
        Movie.objects.create(movie_id=5, tmdb_movie_id=88, tmdb_title="Test1", tmdb_rating=7, year=1983, runtime=120)
        Movie.objects.create(movie_id=6, tmdb_movie_id=44, tmdb_title="Test3", tmdb_rating=5, year=2004, runtime=120)

        Rate.objects.create(rate_id=1, rate=1)
        Rate.objects.create(rate_id=3, rate=3)
        Rate.objects.create(rate_id=4, rate=4)

        Rating.objects.create(rating_id=1, user_id=1, movie_id=3, rate_id=4)
        Rating.objects.create(rating_id=2, user_id=1, movie_id=2, rate_id=3)
        Rating.objects.create(rating_id=3, user_id=2, movie_id=1, rate_id=1)
        Rating.objects.create(rating_id=4, user_id=2, movie_id=4, rate_id=4)

        MovieList.objects.create(movie_list_id=1, movie_id=3, list_id=3)
        MovieList.objects.create(movie_list_id=2, movie_id=2, list_id=3)
        MovieList.objects.create(movie_list_id=5, movie_id=5, list_id=3)
        MovieList.objects.create(movie_list_id=6, movie_id=6, list_id=3)

        MovieList.objects.create(movie_list_id=3, movie_id=1, list_id=6)
        MovieList.objects.create(movie_list_id=4, movie_id=4, list_id=6)

    def test_should_return_formated_dataset(self):
        self.assertEqual(CollaborativeFiltering.get_dataset(), {1: {3: 4, 2: 3, 5: 0, 6: 0}, 2: {1: 1, 4: 4}})

    @mock.patch('moviemancer.collaborative_filtering.CollaborativeFiltering.person_correlation')
    def test_should_call_pearson_on_generate_prediction(self, mock_person_correlation):
        mock_person_correlation.return_value = 0.98
        CollaborativeFiltering.generate_prediction(person=1)
        mock_person_correlation.assert_called()

    def test_should_return_value_between_minus_one_and_one(self):
        result = CollaborativeFiltering.person_correlation(person1=1, person2=2, dataset=CollaborativeFiltering.get_dataset())
        self.assertGreater(result, -1)
        self.assertLess(result, 1)