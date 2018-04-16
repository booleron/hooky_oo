# -*- coding: utf-8 -*-

import os
from time import gmtime, strftime

import tweepy
import requests
from bs4 import BeautifulSoup

# ====== Individual bot configuration ==========================
bot_username = os.environ['LOG_NAME']
logfile_name = bot_username + ".log"
# ==============================================================


def create_tweet():
    """
    Retrieve haiku and return it
    :return: str
    """
    request = requests.get('https://randomhaiku.com/').text
    soup = BeautifulSoup(request, 'lxml')

    lines = soup.find_all('line')
    haiku = '\n'.join([line.text for line in lines])

    return haiku


def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
    auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)
    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        log(e.message)
        print(e)
    else:
        log("Tweeted:\n" + text)


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)


if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)
