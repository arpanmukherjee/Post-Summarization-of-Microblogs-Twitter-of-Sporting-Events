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
        try:
            with open('UC19WC.json', 'a') as f:
                f.write(data)
                return True
            # decoded_data = json.loads(data)
            # f = open('SAvsIND.json', 'wb')
            # json.dump(decoded_data, f, sort_keys=True, indent=4)
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print status
        return True




def start_stream(auth):
    while True:
        try:
            stream = Stream(auth, StdOutListener())
            stream.filter(track=['UC19CWC','ICCU19CWC','AUSvIND','INDvAUS','UC19WCFinal','U19WorldCupFinal'])
        except:
            continue


auth = OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
start_stream(auth)
