#http://socialmedia-class.org/twittertutorial.html
import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '3580075461-fo5tkkpHU1uJzqlnS1bKFRIHhZ8AHpteeEMpqcb'
ACCESS_SECRET = 'qoQ9zf3w6nMCkw0PTnkIGu4MW8qZO0lakZktzxPTkrpl6'
CONSUMER_KEY = 'LIPK2LrBmdaAW5Jr9xGVq5SoQ'
CONSUMER_SECRET = '5gAwRXRpdveauCTpVn3ms3BjVCSf48Ivko79KHmB1D8XlE4T1s'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break
    
print('Printing search tweets')

twitter = Twitter(auth=oauth)

s_t = twitter.search.tweets(q='#nlproc')

#for search_tweet in twitter.search.tweets(q='#nlproc'):
print json.dumps(s_t, indent=4)