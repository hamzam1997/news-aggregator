from django.test import TestCase
from news.models import Query, QueryResult

import pytz
class TestModels(TestCase):

    def setUp(self):
        self.query = Query.objects.create()
    
    def test_query_timestamp_is_aware(self):
        """Tests if the query model is being created with timezone-aware timestamp
        """
        self.assertEquals(Query.objects.get(query = None).queriedAt.tzinfo, pytz.utc)
        