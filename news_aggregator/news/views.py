from django.shortcuts import render
from django.http import JsonResponse

from .ThirdPartyAPIFunctions import getPosts
# Create your views here.

def getNews(request):
    query = request.GET.get('query')
    response = getPosts(query)
    return JsonResponse(response, safe = False)