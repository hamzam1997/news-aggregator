from django.test import TestCase, Client
from django.urls import reverse
from django.utils.timezone import make_aware
from django.http import JsonResponse

from news.models import Query, QueryResult

import datetime
import pytz

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.getNews_url = reverse('getNews')

    def test_query_response_in_json(self):
        response = self.client.get(self.getNews_url)
        self.assertEquals(type(response), JsonResponse)

    def test_query_blank(self):
        response = self.client.get(self.getNews_url)
        self.assertEquals(response.status_code, 200)

    def test_query_with_paramaters(self):
        response = self.client.get(self.getNews_url, {'query':"test"})
        self.assertEquals(response.status_code, 200)
    
    def test_query_timestamp_is_aware(self):
        response = self.client.get(self.getNews_url)
        self.assertEquals(Query.objects.get(query = None).queriedAt.tzinfo, pytz.utc)

    def test_query_retain_timestamp(self):
        old_timestamp = make_aware(datetime.datetime.now())
        Query.objects.create(query = None, queriedAt = old_timestamp)
        response = self.client.get(self.getNews_url)
        new_timestamp = Query.objects.get(query = None).queriedAt
        self.assertEquals(old_timestamp, new_timestamp)
    
    def test_query_update_timestamp(self):
        old_timestamp = make_aware(datetime.datetime.now() - datetime.timedelta(hours = 1))
        Query.objects.create(query = None, queriedAt = old_timestamp)
        response = self.client.get(self.getNews_url)
        new_timestamp = Query.objects.get(query = None).queriedAt
        self.assertNotEquals(old_timestamp, new_timestamp)

    def test_queryResult_retain(self):
        queryResult = QueryResult.objects.create(
            headline = "test",
            link = "test.com",
            source = "testSource"
        )
        query = Query.objects.create(query = None, queriedAt = make_aware(datetime.datetime.now()))
        query.results.add(queryResult)
        response = self.client.get(self.getNews_url)
        query = Query.objects.get(query = None)
        newQueryResult = query.results.all()[0]
        self.assertEquals(queryResult, newQueryResult)

    def test_queryResult_update(self):
        old_timestamp = make_aware(datetime.datetime.now() - datetime.timedelta(hours = 1))
        queryResult = QueryResult.objects.create(
            headline = "test",
            link = "test.com",
            source = "testSource"
        )
        query = Query.objects.create(query = None, queriedAt = old_timestamp)
        query.results.add(queryResult)
        response = self.client.get(self.getNews_url)
        query = Query.objects.get(query = None)
        newQueryResult = query.results.all()[0]
        self.assertNotEquals(queryResult, newQueryResult)





