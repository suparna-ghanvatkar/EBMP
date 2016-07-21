import tweepy

auth = tweepy.OAuthHandler('NJum7uhK5zr40OG4lv6chSwBI','FmH8hYIZ5kMKeDf7TEwWVaVUJkk9duOFDJMUY1clQdgJEKYqKQ')
auth.set_access_token('2988845713-YDyZehWDMweatZ2FFF97VrsU3b5DAJ2qbfqmgAw', 'JnQRN2kfo9sYGCPbrg7VI7aYYkiDMi9AnlQOdMDFhaYlI')

api = tweepy.API(auth)

def ret_tweet(usnm):
	count=0
	info=api.user_timeline(usnm)
	return info[0].text
	'''for tweet in info:
		count=count+1	
		print tweet.text 
		print tweet.created_at
		print "\n"
	print info[count-1].text
	print info.text
	'''


