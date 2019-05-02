import threading
from telethon import TelegramClient
import app
from flask_socketio import emit 
from app import socketio, tg_info
from threading import Lock, Event
from queue import Queue
import asyncio

id_ = tg_info.id_ 
h = tg_info.hash_
client = TelegramClient('first_attempt', id_, h)
app = app.app

lock = Lock() # all the threading stuff
event_to_flask = threading.Event()
event_to_async = threading.Event()
queue = Queue() 
one_more_queue = Queue()
kek1 = Event()
kek2 = Event()

class tg_thread(threading.Thread):
	def __init__(self, client):
		threading.Thread.__init__(self)
		self.daemon = True
		self.client = client
	def run(self):
		self.client.run_until_disconnected()

class message_sender(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.client = None
		self.daemon = True

	def starting(self):
		self.client = TelegramClient('sending', id_, h)
		self.client.connect()
		
	def run(self):
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		
		async def main():
			obj, msg = one_more_queue.get()
			client1 = TelegramClient('sending', id_, h, loop = loop)
			await client1.connect()
			await client1.send_message(obj, message = msg)					
			await client1.disconnect()
		
		loop.run_until_complete(main())
		
tg = tg_thread(client) 	


