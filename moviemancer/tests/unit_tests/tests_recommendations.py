from django.test import TestCase
from moviemancer.reco_refactor import convert_tmdb_rating
from moviemancer.models import Viwer, Movie

class RecommendationTestCase(TestCase):

    def test_should_convert_tmdb_rating_to_five(self):
        self.assertEquals(convert_tmdb_rating(9),5)

    def test_should_convert_tmdb_rating_to_four(self):
        self.assertEquals(convert_tmdb_rating(8.8),4)