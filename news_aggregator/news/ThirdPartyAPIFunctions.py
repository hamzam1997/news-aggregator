from newsapi import NewsApiClient
import praw


newsapi = NewsApiClient("6fc8fbebbb8d48859431e23e20ef264b")

reddit = praw.Reddit(client_id='ea4HN792BzUdOQ', \
                     client_secret='zH-1JdgfVEv1Xg1KctjAi9KvG28', \
                     user_agent='news-aggregator'
                     )

def getPostsFromNewsAPI(query = None):
    top_headlines = newsapi.get_top_headlines(q = query, category = 'general')
    cleanedArticles = []
    for i in top_headlines["articles"]:
        news = {"headline":i["title"],
                "link": i["url"],
                "source":"newsapi"
                }
        cleanedArticles.append(news)
    return cleanedArticles


def getPostsFromReddit(query = None):
    posts = None
    if query in [None, ""]:
        posts = reddit.subreddit('news').hot(limit = 100)
    else:
        posts = reddit.subreddit('news').search(query)

    
    cleanedPosts = []
    for post in posts:
        news = {"headline": post.title,
                "link": post.url,
                "source":"reddit"
                }
        cleanedPosts.append(news)
    return cleanedPosts

def getPosts(query = None):
    return getPostsFromNewsAPI(query) + getPostsFromReddit(query)