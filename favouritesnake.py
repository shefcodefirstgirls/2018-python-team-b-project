import tweepy

consumer_key = 'xxxxx'
consumer_secret = 'xxxxx'
access_token = 'xxxxx'
access_token_secret = 'xxxxx'

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
