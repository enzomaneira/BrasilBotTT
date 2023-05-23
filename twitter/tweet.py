import tweepy

api = tweepy.Client(
    consumer_key='vrmBJaTmT7BTVNxu2Ug01IPeF',
    consumer_secret='RShYK0w57SHbVqAcce0Dt4HTvnmvB07zqrLzAIivwddTV4ukMo',
    access_token='1660829085445025793-t39jQbO3DCmX9GQHFnzKzecfzjoL2L',
    access_token_secret='O3jUFHL5W8UqgDR8mFOKZKWHFEYDVtnP6MLGv8TVLkluR',
)

try: 
    tweeet = api.create_tweet(text='oi site')
    print(tweeet)
except:
    print("Houve falha!")