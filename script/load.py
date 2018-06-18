# import required packages
import tweepy  
import sys  
import json    
import csv
from textwrap import TextWrapper
from textblob import TextBlob
from datetime import datetime  
from elasticsearch import Elasticsearch
from tweepy.streaming import StreamListener
import os
import io
import time

# Add twitter applications api Keys
consumer_key="CRq4AJCIlp679vvym4ZoQ4NtV"  
consumer_secret="Cu3i9uCGl7fEWg0uSMYW2ZFcxJ0W46bjFXb5C2tsBeq0EQeu36"
access_token="2989860038-WFohQVYtVZlG3ndo4Nd1CBjmg7LJJf1yghLj45g"  
access_token_secret="zQOx1OfHFhQJbiVDtXo1ZMVQjzrAopEamFCuhghTmCLlX"

# create Elasticsearch client
es = Elasticsearch() # use default of localhost, port 9200
# Authorization Handlers with access tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# overriding tweepy.StreamListener to add logic to on_status
class StreamListener(tweepy.StreamListener):
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        # get author's name,time and message of tweet 
        try:
            doc = {
                "author": status.author.screen_name,
                "date": status.created_at,
                "message": status.text
            }
            # store this index with document body in Elasticsearch 
            res = es.index(index='my-tweets', doc_type='tweet', body=doc)
            print(res)

        except Exception as e:
            pass

    # Handling Errors
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        if status_code == 403:
            print("The request is understood, but it has been refused or access is not allowed. Limit is maybe reached")
            return False

# api to stream
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=10, retry_delay=5, retry_errors=5)
# stream object
myStreamListener = StreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
# Starting a Stream with certain keywords with Async Streaming
myStream.filter(languages=["en"], track=['python','html','javascript','java','nodejs','elasticsearch','c++','stackoverflow','MongoDB'], async=True)

# Useful Links:
# ElasticSearch Data : http://localhost:9200/_cat/indices?v
# Search : http://localhost:9200/my-tweets/_search?q='input query'&size=100