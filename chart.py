import matplotlib.pyplot as plt
import requests
import json

# Elasticsearch endpoint
endpoint = "http://localhost:9200/tweets_dataset/_search"

# Elasticsearch query
query = {
    "size": 0,
    "aggs": {
        "sentiment_distribution": {
            "histogram": {
                "field": "sentiment",
                "interval": 1
            }
        }
    }
}

# Send request to Elasticsearch
response = requests.get(endpoint, json=query)

# Check if request was successful
if response.status_code == 200:
    # Load response as JSON
    response_json = json.loads(response.text)

    # Extract sentiment distribution from response
    sentiment_distribution = response_json["aggregations"]["sentiment_distribution"]["buckets"]

    # Extract sentiment values and counts from sentiment distribution
    sentiment_values = [bucket["key"] for bucket in sentiment_distribution]
    sentiment_counts = [bucket["doc_count"]
                        for bucket in sentiment_distribution]

    # Plot sentiment distribution
    plt.bar(sentiment_values, sentiment_counts)
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()
else:
    print("Request failed with status code:", response.status_code)
