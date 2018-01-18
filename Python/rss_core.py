import feedparser
import urllib

emotion = 2



# Emotion = 0 --> Normal
# Emotion = 1 --> Cheerful
# Emotion = -1 --> Sad
# Emotion = 2 --> Bored
# EMotion = -2 --> Depressed

toi_top = feedparser.parse(r'https://timesofindia.indiatimes.com/rssfeedstopstories.cms')
for post in toi_top.entries:
    print(toi_top['feed']['description'])

feed https://news.ycombinator.com/rss