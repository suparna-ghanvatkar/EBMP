import pickle,random,time
'''
Data structures definitions:
list of all the users to behave as a lookup for the dictionary of theobject name of class User. A default dictionary is made for the case the record for the user doesnt exist.
'''
user_dict={'suparna':'usr0','rohit':'usr1','aditi':'usr2','sagar':'usr3'}
default_sad=['song0','song1','song2','song3','song4']
default_happy=['song5','song6','song7','song8']
default_neutral=['song9','song10','song11','song12']
emotion="happy"
Usr=""
playlist=[]
played=[]
flag=0

class User:
	def __init__(self,name):
		self.name=name
	song_sad={}
	song_happy={}
	song_neutral={}
	def printusr(self):
		print self.name
	
'''
Function to add other users lists having the given song
'''
def find_more_playlists(usr,song):
	print playlist
	for i in users:
		if i==usr:
			continue
		elif (song in i.song_sad):
			playlist.append(i.song_sad.keys())	
		elif (song in i.song_happy):
			playlist.append(i.song_happy.keys())	
		elif (song in i.song_neutral):
			playlist.append(i.song_neutral.keys())
		#playlist.remove((song))	

def add_list(user,emotionlist,emo):
	if len(emotionlist)>0 and flag==0:
		playlist.append((emotionlist.keys()))
		flag=1
	else:
		default="default_"+emo
		playlist.append((eval(default)))
	print playlist

'''
Recommender:
	add list to playlist
	song played then add similar list
		else remove the list from playlist
'''
def recomm(user,emotionlist,emo):
	add_list(user,emotionlist,emo)
	while(len(playlist)>0):
		if playlist[0][0]==[]:
			playlist.pop(0)
		if playlist[0][0] in played:
			playlist[0].pop(0)
			if playlist[0][0]==[]:
				playlist.pop(0)
		stat=play(playlist[0][0])
		if stat=='c':
			song=playlist[0][0]
			print emotionlist
			if song in emotionlist.keys():
				k=emotionlist[song]
				emotionlist[song]=k+1
			else:
				emotionlist[song]=1
			played.append(song)
			find_more_playlists(user,playlist[0][0])
			playlist[0].pop(0)
		else:	
			playlist.pop(0)
		#print playlist
	if(len(playlist)==0):
		recomm(user,emotionlist,emo)

'''
Abstraction layer: 
Test abstraction:
Print the song that would be played and accept input from user as listened or not listened
'''
def play(song):
	print "Playing ",song
	stat=raw_input()
	return stat

'''
Get the param as the username and the emotion of the user and stream the music accordingly to the server
'''
def get_info(usr,emo):
	global emotion,Usr
	emotion=emo
	Usr=usr

def play_music(usr):
	global emotion
	objnm=user_dict[usr]
	o=eval(objnm)
	o.printusr()
	emo_list=objnm+".song_"+str(emotion)
	emotionn=eval(emo_list)
	recomm(o,emotionn,emotion)

'''
usr0=pickle.load(open('./userdb/usr0.txt','rw'))
usr1=pickle.load(open('./userdb/usr1.txt','rw'))
usr2=pickle.load(open('./userdb/usr2.txt','rw'))
usr3=pickle.load(open('./userdb/usr3.txt','rw'))
'''
def config():
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
	users=[usr0,usr1,usr2,usr3]
	get_info('suparna','sad')
	play_music('suparna')



'''
Abstraction layer:
Music API:
Stream the music or send the music to be played to the server which will play the music
'''
def play(song):
	return 
