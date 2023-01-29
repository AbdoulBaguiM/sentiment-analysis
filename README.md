# Twitter Sentiment Analysis

This repository contains two Python scripts that perform sentiment analysis on recent tweets containing a given keyword. The sentiment polarity of each tweet is extracted using TextBlob and stored in an Elasticsearch index. The second script aggregates the sentiment values stored in Elasticsearch and plots a bar graph of the sentiment distribution.

## Requirements

- docker
- requests
- textblob
- matplotlib

## Usage

1. Start Elasticsearch and Kibana containers by running

   docker-compose up -d

2. Replace the bearer_token in the first script with a valid Twitter API token.
3. Run the first script to index the sentiment of recent tweets containing the query "marvel".
4. Run the second script to visualize the sentiment distribution of the indexed tweets.

## File descriptions

1. script.py: Indexes the sentiment of recent tweets containing the query "marvel".
2. chart.py: Aggregates the sentiment values stored in Elasticsearch and plots a bar graph of the sentiment distribution.

## Further Information

For more detailed information on this project, see the following Medium articles:

[Sentiment Analysis of Tweets with Elasticsearch](https://medium.com/@mhdabdel151/sentiment-analysis-of-tweets-with-elasticsearch-879407976baf)
[Sentiment Analysis of Tweets with Elasticsearch (part2)](https://medium.com/@mhdabdel151/sentiment-analysis-of-tweets-with-elasticsearch-part2-e921d568bb44)
[Sentiment Analysis of Tweets with Elasticsearch (part3)](https://medium.com/@mhdabdel151/sentiment-analysis-of-tweets-with-elasticsearch-part3-93133d9dae30)
