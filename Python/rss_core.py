import feedparser
import urllib
import newspaper3k
emotion = 2

# Code to change emotion goes here.

# Emotion = 0 --> Normal
# Emotion = 1 --> Cheerful
# Emotion = -1 --> Sad
# Emotion = 2 --> Bored
# EMotion = -2 --> Depressed

reuters = newspaper.build('https://in.reuters.com/')
if (emotion == 2):
    for article in reuters.articles:
    	print(article.url)
