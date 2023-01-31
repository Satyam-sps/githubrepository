import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


access_key= "PtjPcDXaZbcgVhGT9owNNj9AK"
access_secret = "L7x8E4Q2JduZ1wOP7ThUBlK9lFUn0qQG7bpjgZeQEyZJGzxVUl"
consumer_key = "808737599410110464-5BgVzeoSLOrWL9XzJEhLQTlmmopB4gg"
consumer_secret="CTymw5azVMKoKkfLYrqg6KW2zweryM630CMOLWjQu9kfI"


auth = tweepy.OAuthHandler(access_key,access_secret)
auth.set_access_token(consumer_key,consumer_secret)

api = tweepy.API(auth)

tweets = api.user_timeline(
    screen_name = "@kamnagar",
    count = 200,
    include_rts = False
)

print(tweets)