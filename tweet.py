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

# Loop principal
while True:
    now = datetime.now()
    if now.hour == 7 and now.minute == 0:
        # Chame a função enviar_tweet com o texto que você deseja postar
        enviar_tweet(mensagem)
        print("Tweet enviado.")
        # Espere 24 horas antes de enviar o próximo tweet
        time.sleep(24 * 60 * 60)
    else:
        # Aguarde 60 segundos antes de verificar a hora novamente
        time.sleep(60)

