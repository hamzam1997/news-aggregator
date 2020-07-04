from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import make_aware
from django.conf import settings

from .ThirdPartyAPIFunctions import getPosts
from .models import Query, QueryResult

import datetime

# Create your views here.

REFRESH_HOURS = settings.REFRESH_HOURS

def updateResults(queryObject, query):
    """Updates the results by fetching the queries from APIs

    Retrieves the posts from the APIs based on the query from the user. 
    Creates a models.QueryResult object for every post and attaches with the
    models.Query object passed in the parameter

    :param queryObject: The object to which the fetched results have to be attached
    :type queryObject: models.Query
    :param query: The query to fetch the results for
    :type query: str
    """

    queryObject.results.all().delete()
    posts = getPosts(query)
    for post in posts:
        queryResult, created = QueryResult.objects.get_or_create(   headline = post["headline"],
                                            link = post["link"],
                                            source = post["source"]
                                        )
        queryObject.results.add(queryResult)


def getNews(request):
    """View method mapped on the url.

    It handles the request and responds accordingly by by checking the
    expiry time of the query if query has been sent before, and also for the new query.

    :param request: The request made from the client side
    :type request: django.http.HttpRequest
    :return: A response in json format containing the list of all results
    :rtype: django.http.JsonResponse
    """
    query = request.GET.get('query')
    obj, created = Query.objects.get_or_create(
        query = query
    )
    if not created:
        currentTime = make_aware(datetime.datetime.now())
        difference = currentTime - obj.queriedAt

        if (difference.seconds/60) > (REFRESH_HOURS * 60) - 1:
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