from django.db import models
from django.utils.timezone import make_aware

import datetime

# Create your models here.

class QueryResult(models.Model):
    headline = models.CharField(max_length = 1000)
    link = models.URLField()
    source = models.CharField(max_length = 30)

    def as_dict(self):
        """
        :return: Returns the model object as a dictionary with each attribute as a key.
        :rtype: dict
        """
        return {
            "headline": self.headline,
            "link": self.link,
            "source": self.source
        }

class Query(models.Model):
    query = models.CharField(max_length = 100, null = True, blank = True)
    queriedAt = models.DateTimeField(default = make_aware(datetime.datetime.now()))
    results = models.ManyToManyField(QueryResult)