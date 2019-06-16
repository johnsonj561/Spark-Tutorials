import os
import socket
import json
import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_secret = os.environ['TWITTER_ACCESS_SECRET']

class TweetListener(StreamListener):
    def __init__(self, csocket):
        self.client_socket = csocket
    
    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text']).encode('utf-8')
        except BaseException as e:
            print('Error', e)
        return True
    
    def on_error(self, status):
        print('Status', status)
        return True


def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    twitter_stream = Stream(auth, TweetListener(c_socket))
    twitter_stream.filter(track=['nike'])

if __name__ == '__main__':
    s = socket.socket()
    host = '127.0.0.1'
    port = 9000
    s.bind((host,port))
    print('listening on port', port)
    
    s.listen(5)
    c, addr = s.accept()
    
    sendData(c)

