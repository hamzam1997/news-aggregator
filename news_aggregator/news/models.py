from django.db import models

# Create your models here.
class Query(models.Model):
    query = models.CharField(max_length = 100)
    queriedAt = models.DateTimeField(auto_now = True)

class QueryResult(models.Model):
    headline = models.CharField(max_length = 1000)
    url = models.URLField()
    source = models.CharField(max_length = 30)
    queries = models.ManyToManyField(Query)