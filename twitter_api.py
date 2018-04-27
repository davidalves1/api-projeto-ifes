import env
import twitter

class TwitterApi(object):
    def __init__(self):
        self.api = twitter.Api(
            consumer_key=env.TWITTER_CONSUMER_KEY,
            consumer_secret=env.TWITTER_CONSUMER_SECRET,
            access_token_key=env.TWITTER_ACCESS_TOKEN,
            access_token_secret=env.TWITTER_ACCESS_TOKEN_SECRET
        )

    def publish(self, message):
        self.api.PostUpdate(message)