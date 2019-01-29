from django.test import TestCase
from moviemancer.helpers import Helpers
from moviemancer.models import Viwer, Type, List

class HelpersTestCase(TestCase):
    def setUp(self):
        Viwer.objects.create(user_id=1, name="hermoione", email="batata@batatinha.com")

        Type.objects.create(type_id=1, type_name="recommendation")
        Type.objects.create(type_id=2, type_name="watchlist")
        Type.objects.create(type_id=3, type_name="watchedlist")

        List.objects.create(list_id=1, user_id=1, type_id=1)
        List.objects.create(list_id=2, user_id=1, type_id=2)
        List.objects.create(list_id=3, user_id=1, type_id=3)

    def test_should_return_list_by_user(self):
        self.assertEqual(Helpers.get_user_list_id_by_type_id(user_id=1, type_id=3), 3)

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
