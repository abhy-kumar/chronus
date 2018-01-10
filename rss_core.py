import feedparser

emotion = 0
print(emotion)
# Code to change emotion goes here.

# Emotion = 0 --> Normal
# Emotion = 1 --> Cheerful
# Emotion = -1 --> Sad
# Emotion = 2 --> Bored
# EMotion = -2 --> Depressed

#def ch_emo:


if (emotion == 2):
	t = feedparser.parse('http://feeds.reuters.com/reuters/oddlyEnoughNews')
	for post in t.entries:
    	print(post.title + '\n : ' + post.link + '\n')

