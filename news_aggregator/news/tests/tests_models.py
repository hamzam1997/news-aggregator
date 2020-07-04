from django.test import TestCase
from news.models import Query, QueryResult

import pytz
class TestModels(TestCase):

    def setUp(self):
        self.query = Query.objects.create()
    
    def test_query_timestamp_is_aware(self):
        self.assertEquals(Query.objects.get(query = None).queriedAt.tzinfo, pytz.utc)
        