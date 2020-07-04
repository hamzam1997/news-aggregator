from django.test import SimpleTestCase
from django.urls import reverse, resolve
from news.views import getNews

class TestUrls(SimpleTestCase):

    def test_getViews_url_is_resolves(self):
        url = reverse('getNews')
        self.assertEquals(resolve(url).func, getNews)

    
