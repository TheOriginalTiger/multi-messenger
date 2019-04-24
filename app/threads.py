import threading
from telethon import TelegramClient
import app
from flask_socketio import emit 
from app import socketio, tg_info
from threading import Lock, Event
from queue import Queue


id_ = tg_info.id_ 
h = tg_info.hash_
client = TelegramClient('first_attempt', id_, h)
app = app.app

lock = Lock() # all the threading stuff
event_to_flask = threading.Event()
event_to_async = threading.Event()
queue = Queue() 

class tg_thread(threading.Thread):
	def __init__(self, client):
		threading.Thread.__init__(self)
		self.daemon = True
		self.client = client
	def run(self):
		self.client.run_until_disconnected()

		
tg = tg_thread(client) 	


