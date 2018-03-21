import tweepy

consumer_key = 'x0jGy3Hx0aBDSvZK7kBkS7y6B'
consumer_secret = 'zVOkrQRwZjDdnVGikJNOld06DBpBVdDHahE2AkGVynJQemCWuT'
access_token = '971448341635784707-9oZobc20SUG6TWJmN2cCeEwb4x4jr2D'
access_token_secret = 'EgDKzGlhLVWapXzEk2zCWdapb9qvqVQXjTSNY3rZssg2y'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)

def show_content(tweets):
    for tweet in tweets:
        print("\n" + tweet.text)

def collect_tweets(keyword):
    keyword = keyword.strip()
    print('Finding tweets with {} keyword'.format(keyword))
    tweets = twitter.search(keyword, lang="en", rpp=1)
    show_content(tweets) 
    return tweets