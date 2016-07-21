from textblob import TextBlob
from tweet import ret_tweet

def get_sentiment(usnm):
	tw=ret_tweet(usnm)
	print tw, ":"
	text=TextBlob("Excited at work!!:)")
	return text.sentiment.polarity
