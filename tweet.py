import tweepy
from resp import mensagem
import time
from datetime import datetime


api = tweepy.Client(
    consumer_key='vrmBJaTmT7BTVNxu2Ug01IPeF',
    consumer_secret='RShYK0w57SHbVqAcce0Dt4HTvnmvB07zqrLzAIivwddTV4ukMo',
    access_token='1660829085445025793-t39jQbO3DCmX9GQHFnzKzecfzjoL2L',
    access_token_secret='O3jUFHL5W8UqgDR8mFOKZKWHFEYDVtnP6MLGv8TVLkluR',
)

def enviar_tweet(texto):
    tweeet = api.create_tweet(text=texto)
    print(tweeet)

while True:
    now = datetime.now()
    if now.hour == 7 and now.minute == 10:
        enviar_tweet(mensagem)
        print("Tweet enviado.")
        time.sleep(24 * 60 * 60)
    else:
        time.sleep(60)

