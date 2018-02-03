import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


access_token = "2822909874-ZJ1vra8PUwN9WeO7gjh52S1jjkPCXLCXdESHZRa"
access_token_secret = "Aio1oFCNXg5d19Eh24KJLaoiCUM9BGdOKc8pWzaFfatFa"
consumer_key = "Lm90f1Did8j2jFV0wIz4zokX8"
consumer_key_secret = "p3aLTqwfWCaD0onbtZcqcqZzufIg4ZRrTDe9QeXaAXobSQmGXz"


class StdOutListener(StreamListener):

    def on_data(self, data):
        decoded_data = json.loads(data)
        f = open('SAvsIND.json', 'wb')
        json.dump(decoded_data, f, sort_keys=True, indent=4)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    listener_obj = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener_obj)

    stream.filter(track=['#SAvsIND'])
