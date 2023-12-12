# pylint: disable-all

import pandas as pd
import tweepy
import os

from datetime import datetime
from dotenv import load_dotenv

ENV_PATH = "./Twitter_API_Creds.env"
load_dotenv(ENV_PATH)

def get_tweets():

    # Twitter Authentication
    auth = tweepy.OAuthHandler(
        access_token=os.environ["ACCESSTOKEN"],
        access_token_secret=os.environ["ACCESSTOKENSECRET"],
        consumer_key=os.environ["CONSUMERAPIKEY"],
        consumer_secret=os.environ["CONSUMERAPIKEYSECRET"],
    )

    api = tweepy.API(auth=auth)

    tweets = api.user_timeline(
        screen_name="@elonmusk", # Twitter Profile
        count=200,  # Number of tweets to extract.
        include_rts=False,  # Incude re-tweets
        tweet_mode="compatible",
    )

    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {
            "user": tweet.user.screen_name,
            "text": text,
            "favorite_count": tweet.favorite_count,
            "retweet_count": tweet.retweet_count,
            "created_at": tweet.created_at
        }

        tweet_list.append(refined_tweet)

    data_df = pd.DataFrame(tweet_list)
    data_df.to_csv("s3://twitter-etl-s3-bucket/twitter_tweets.csv")
