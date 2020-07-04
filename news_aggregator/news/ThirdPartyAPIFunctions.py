from newsapi import NewsApiClient
import praw


newsapi = NewsApiClient("6fc8fbebbb8d48859431e23e20ef264b")

reddit = praw.Reddit(client_id='ea4HN792BzUdOQ', \
                     client_secret='zH-1JdgfVEv1Xg1KctjAi9KvG28', \
                     user_agent='news-aggregator'
                     )

def getPostsFromNewsAPI(query = None):
    """Fetches results from NewsAPI based on the query in parameters.

    Connects to the NewsAPI, fetches the articles. If the query is empty then it fetches the top results, otherwise it fetches the results based on the query.

    :param query: The query to fetch the results for, defaults to None
    :type query: str, optional
    :return: A list of fetched results based on the query in dictionary format
    :rtype: list
    """
    cleanedArticles = []
    try:
        top_headlines = newsapi.get_top_headlines(q = query, category = 'general')
        for i in top_headlines["articles"]:
            news = {"headline":i["title"],
                    "link": i["url"],
                    "source":"newsapi"
                    }
            cleanedArticles.append(news)
        print("Fetched Articles from NewsAPI")
    except Exception as error:
        print(error)
    return cleanedArticles


def getPostsFromRedditAPI(query = None):
    """Fetches results from RedditAPI based on the query in parameters.

    Connects to the RedditAPI, fetches the articles. If the query is empty then it fetches the top results, otherwise it fetches the results based on the query.

    :param query: The query to fetch the results for, defaults to None
    :type query: str, optional
    :return: A list of fetched results based on the query in dictionary format
    :rtype: list
    """
    cleanedPosts = []
    try:
        posts = None
        if query in [None, ""]:
            posts = reddit.subreddit('news').hot(limit = 100)
        else:
            posts = reddit.subreddit('news').search(query)

        for post in posts:
            news = {"headline": post.title,
                    "link": post.url,
                    "source":"reddit"
                    }
            cleanedPosts.append(news)
        print("Fetched Posts from Reddit")
    except Exception as error:
        print(error)
    return cleanedPosts

def getPosts(query = None):
    
    """Fetches results from all the APIs returns a concatenated list of all results fetched.

    Calls getPostsFromNewsAPI and getPostsFromRedditAPI by passing query as the parameter. Concatenates what each function returns and returns the concatenated list.
    
    :param query: The query to fetch the results for, defaults to None
    :type query: str, optional

    :return: A list of fetched results based on the query in dictionary format
    :rtype: list
    """
    return getPostsFromNewsAPI(query) + getPostsFromRedditAPI(query)

