import tweepy 

apiKey = ''
apiKeySecret = ''
accessToken = ''
accessTokenSecret = ''

def OAuth():
    try:
        auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        return auth
    except Exception as e:
        return none

oauth = OAuth()
apicall = tweepy.API(oauth)

apicall.update_status("I wrote this post with the TwitterAPI using Python whoooooooooo")
print("Tweet created")