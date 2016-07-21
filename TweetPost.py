import tweepy

auth = tweepy.OAuthHandler('NJum7uhK5zr40OG4lv6chSwBI','FmH8hYIZ5kMKeDf7TEwWVaVUJkk9duOFDJMUY1clQdgJEKYqKQ')
auth.set_access_token('2988845713-YDyZehWDMweatZ2FFF97VrsU3b5DAJ2qbfqmgAw', 'JnQRN2kfo9sYGCPbrg7VI7aYYkiDMi9AnlQOdMDFhaYlI')

api = tweepy.API(auth)


'''
own timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text'''


#for status
info=api.user_timeline('narendramodi')
for tweet in info:
	print tweet.text 
	print tweet.created_at
	print "\n"



'''
counts and followers
user=api.get_user('Suparna230695')
print user.screen_name
print user.followers_count
print user.tweets
for friend in user.friends():
   print friend.screen_name'''

'''for twt in info:
	print twt.text'''

