from django.test import TestCase
from moviemancer.reco_refactor import convert_tmdb_rating

class RecommendationTestCase(TestCase):

    def test_should_convert_rating_to_five(self):
        self.assertEquals(convert_tmdb_rating(8.8), 4)