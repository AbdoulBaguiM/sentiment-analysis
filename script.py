from elasticsearch import Elasticsearch
import requests
from textblob import TextBlob

es = Elasticsearch(["http://localhost:9200/"])

bearer_token = "AAAAAAAAAAAAAAAAAAAAAA2mjgEAAAAA1WLMD1ox%2Bwt20hWFs47v%2B%2F8t8DA%3DpOQjQ0tYEJYvpU0Vb0MtqZNmKhDeJYwaTpIb1B9M9GkSzdK8oj"

headers = {"Authorization": "Bearer " + bearer_token}


def index_data(data):
    try:
        sentiment = TextBlob(data['text']).sentiment.polarity
        data['sentiment'] = sentiment
        es.index(index="tweets_dataset", body=data)
    except Exception as e:
        print(e)


endpoint_url = "https://api.twitter.com/2/tweets/search/recent"

try:
    params = {"query": "marvel", "max_results": 100}
    response = requests.get(
        endpoint_url, headers=headers, params=params).json()
    for tweet in response["data"]:
        index_data({"text": tweet["text"]})
except Exception as e:
    print(e)
