# News Aggregator
## Description
An application made using Django Framework that aggregates news from Reddit and News API. If the application is running on your localhost. It serves the result in JSON format from an endpoint whenever it gets a request.
### Refresh Rate
The application fetches results if the query is not requested before. If it is requested before, then the application fetches new results only if the last request for a particular query is made after the time of `REFRESH_HOURS` has passed. Otherwise, the application responds with the previously fetched results. The constant `REFRESH_HOURS` is stated at [news_aggregator/news_aggregator/settings.py](news_aggregator/news_aggregator/settings.py)
## Getting Started
### Installation
To install all the requirements run the following command  
`pip install requirements.txt`

### Starting the application
To start the application, go to folder [news_aggregator](news_aggregator) and run the following command  
`python manage.py runserver`

## Usage
Make sure your computer is connected to the internet. After starting the application make request using an application/browser to the url  
`localhost:8000/news`  
To pass the query to the application, pass it as a parameter in the url as  
`localhost:8000/news?query=<your_query>`

### Examples
- Example with no parameter
```
> Request
GET /news   HTTP/1.1
Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ
Accept: application/json

> Response
[
  {
    "headline": "Human organs can be stored for three times as long in major breakthrough for transplants",  // Headline of the article
    "link": "https://www.telegraph.co.uk/science/2019/09/09/human-organs-can-stored-three-times-long-major-breakthrough/",  // Link of the article
    "source": "reddit" // Source that you retrieved this news from
  },
  {
    "headline": "Depth of Field: The Shared Memory of One World Trade Center",
    "link": "https://www.wired.com/story/one-world-trade-center-history-future/",
    "source": "newsapi"
  },
]
```
- Example with query parameter
```
> Request
GET /news?query=bitcoin   HTTP/1.1
Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ
Accept: application/json

> Response
[
  {
    "headline": "IRS goes after cryptocurrency owners for unpaid taxes",
    "link": "https://www.cbsnews.com/news/own-bitcoin-irs-pursues-cryptocurrency-owners-for-unpaid-taxes/",
    "source": "reddit"
  },
  {
    "headline": "Skirting US sanctions, Cubans flock to cryptocurrency to shop online, send funds",
    "link": "https://www.channelnewsasia.com/news/business/skirting-us-sanctions--cubans-flock-to-cryptocurrency-to-shop-online--send-funds-11901148",
    "source": "newsapi"
  },
]
```

## Documentation
The documentation for the code is provided in [news_aggregator/docs/_build/html](news_aggregator/docs/_build/html).
The main page for the documentation is located at [news_aggregator/docs/_build/html/index.html](news_aggregator/docs/_build/html/index.html)

