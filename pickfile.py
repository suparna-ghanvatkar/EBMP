import pickle
class User:
	def __init__(self,name):
		self.name=name
	song_sad={}
	song_happy={}
	song_neutral={}
	def printusr(self):
		print self.name

usr0=User('suparna')
usr1=User('rohit')
usr2=User('aditi')
usr3=User('sagar')
usr1.song_sad={'song1':3,'song2':1,'song5':1}
usr1.song_happy={'song6':3,'song4':4,'song0':1}
usr1.song_neutral={'song9':3,'song12':1,'song8':2}
usr1.song_sad={'song0':3,'song2':1,'song5':1}
usr1.song_happy={'song6':3,'song4':4,'song1':1}
usr1.song_neutral={'song9':3,'song12':1,'song8':2}
pickle.dump(usr0,open('./userdb/usr0.txt','w'))
pickle.dump(usr1,open('./userdb/usr1.txt','w'))
pickle.dump(usr2,open('./userdb/usr2.txt','w'))
pickle.dump(usr3,open('./userdb/usr3.txt','w'))
