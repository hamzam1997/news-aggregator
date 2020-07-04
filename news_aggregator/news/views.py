from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import make_aware

from .ThirdPartyAPIFunctions import getPosts
from .models import Query, QueryResult

import datetime
# Create your views here.
def updateResults(queryObject, query):
    queryObject.results.all().delete()
    posts = getPosts(query)
    for post in posts:
        queryResult, created = QueryResult.objects.get_or_create(   headline = post["headline"],
                                            link = post["link"],
                                            source = post["source"]
                                        )
        queryObject.results.add(queryResult)

def getNews(request):
    query = request.GET.get('query')
    obj, created = Query.objects.get_or_create(
        query = query
    )
    if not created:
        currentTime = make_aware(datetime.datetime.now())
        difference = currentTime - obj.queriedAt

        if (difference.seconds/60) > 59:
            Query.objects.filter(query = query).update(queriedAt = currentTime)
            print("Fetching new results for query")
            updateResults(obj, query)

    else:
        print("Fetching results for new query")
        updateResults(obj, query)

    response = []
    for post in obj.results.all():
        response.append({   "headline": post.headline,
                            "link": post.link,
                            "source": post.source
                        })

    return JsonResponse(response, safe = False)