from django.test import TestCase
from moviemancer.queries import get_list_id_by_user
from moviemancer.models import *

class QueriesTestCase(TestCase):
    def setUp(self):
        Viwer.objects.create(name="hermoione")
        Viwer.objects.create(name="luna")

        Type.objects.create(type_name="recommendation")
        Type.objects.create(type_name="watchlist")
        Type.objects.create(type_name="watchedlist")

        List.objects.create(user_id=1, type_id=1)
        List.objects.create(user_id=1, type_id=2)
        List.objects.create(user_id=1, type_id=3)

        List.objects.create(user_id=2, type_id=1)
        List.objects.create(user_id=2, type_id=2)
        List.objects.create(user_id=2, type_id=3)

    def test_should_return_list_ids_by_user(self):
        list_ids_by_user = set(get_list_id_by_user(1))

        self.assertEquals(len(list_ids_by_user),3)