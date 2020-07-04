# news.tests package

## Models Tests


### class news.tests.tests_models.TestModels(methodName='runTest')
Bases: `django.test.testcases.TestCase`


#### setUp()
Hook method for setting up the test fixture before exercising it.


#### test_query_timestamp_is_aware()
Tests if the query model is being created with timezone-aware timestamp

## Views Tests


### class news.tests.tests_views.TestViews(methodName='runTest')
Bases: `django.test.testcases.TestCase`


#### setUp()
Hook method for setting up the test fixture before exercising it.


#### test_queryResult_retain()
Tests if query retains all results of type models.QueryResult if a request is made before REFRESH_HOURS since the query was updated


#### test_queryResult_update()
Tests if query updatess all results of type models.QueryResult if a request is made after REFRESH_HOURS since the query was updated


#### test_query_blank()
Tests if the response is succesful if request has no parameters


#### test_query_response_in_json()
Tests if the response is in json format


#### test_query_retain_timestamp()
Tests if query doesn’t get update if a request is made before REFRESH_HOURS since the query was updated


#### test_query_timestamp_is_aware()
Tests if the request can create a models.Query object with timezone-aware timestamp


#### test_query_update_timestamp()
Tests if query gets updated if a request is made after REFRESH_HOURS since the query was updated


#### test_query_with_parameter()
Tests if the response is succesful if request has query paramter

## Urls Tests


### class news.tests.tests_urls.TestUrls(methodName='runTest')
Bases: `django.test.testcases.SimpleTestCase`


#### test_getViews_url_is_resolves()
Tests if the url is resolved and returns the function views.getNews
