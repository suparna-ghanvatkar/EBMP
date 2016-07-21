import tornado.ioloop
import tornado.web
from sentiment import get_sentiment
from music_recc import get_info
from show_text import filtering
from text_msg import getVars

emo=""
nm=""
song="music.mp3"
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",)
    def post(self):
		nm=self.get_argument('user')
		psw=self.get_arguments('pass')
		if psw=="12345":
			self.redirect("/home")
		else:
			self.write('404 Error!')

class SentimentHandler(tornado.web.RequestHandler):
	def get(self):
		rsong=open("./song.txt","r")
		song=rsong.read()
		self.render("chat.html",song_url=song)
	def post(self):
		tw=self.get_argument('twitter')
		frm=self.get_argument('from')
		to=self.argument('to')
		msg=self.argument('message')
		getVars(msg,to,frm)
		if msg=="":
			pol1=get_sentiment(tw_nm)
		if twitter=="":
			MSG=filtering(to)		
			pol2=get_sentiment(MSG)
		if pol1==0:
			pol=pol2
		elif pol2==0:
			pol==pol1
		else:
			pol=(pol1+pol2)/2
		if pol>0:
			emo="happy"
		elif pol<0:
			emo="sad"
		elif pol==0:
			emo="neutral"
		get_info(nm,emo)

class NextSongHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("home.html")
		

application = tornado.web.Application([
    (r"/", MainHandler),
	(r"/home",SentimentHandler),
	(r"/next",NextSongHandler)	
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
