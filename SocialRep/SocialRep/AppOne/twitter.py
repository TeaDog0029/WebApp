from twython import Twython

# Credentials given by Twitter
APPLICATION_NAME = "HashTagS34rch"
CONSUMER_KEY = "DQ0erinhabFAofKpXwjcNgRfw"
CONSUMER_SECRET = "H58G2BKwrgt8nXnuZxWWTmup4MquukIhp7jcCT9JrHiFyPJcEC"
ACCESS_TOKEN ="1093173588-UqoDpGjohJ7a3XZZhIPdxUHl8dUjoJw6W6FauMb"
ACCESS_TOKEN_SECRET ="QF3v4H5bQC2t5UptxtnxRJXXVL05GfjgQ2Pp7x6OQTrNy"
OWNER = "TeaDog29"
OWNER_ID = "1093173588"

def queryTwitter(string, number): # number must be lower than 100
    t = Twython(app_key=CONSUMER_KEY, 
                app_secret=CONSUMER_SECRET, 
                oauth_token=ACCESS_TOKEN, 
                oauth_token_secret=ACCESS_TOKEN_SECRET)
    search = t.search(q= string, result_type = 'recent', count = number)
    tweets = search['statuses']
    list_tweets = []
    tupleT = ()
    for tweet in range(0,number):
        i = tweets[tweet]['text']
        j = (i,) # in views.py, you cannot return a list. I tuple can do...
        tupleT = tupleT+ j
    return tupleT
#search['statuses'][2]['text']


