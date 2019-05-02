from telethon import TelegramClient, sync, events
from telethon.tl.types import User
import logging
import app
import threading
<<<<<<< HEAD
from app import  queue, lock, event_to_async, event_to_flask, socketio, threads 
=======
from app import  queue, lock, event_to_async, event_to_flask, socketio 
>>>>>>> e0599a6c8a6fb3af42d9bd8c8393ed44f387d3fb
from flask_socketio import emit
from datetime import datetime
from time import sleep

client = app.client 

class dialog_():	
	def __init__(self, dia_obj):
		self.obj = 	dia_obj
		self.id_ = dia_obj.id
		self.hash = dia_obj.entity.access_hash
		self.messages = [] 
<<<<<<< HEAD
		self.senders = []
		self.name = self.obj.name
		for message in client.iter_messages(self.obj, limit = 10):
			self.messages.append(message.message)
			if self.obj.id != client.get_me().id:
				if message.sender.last_name:
					self.senders.append(str(message.sender.first_name + ' ' + message.sender.last_name))
				else:
					self.senders.append(message.sender.first_name)
			else:
				user = client.get_me()
				if user.last_name:
					self.senders.append(user.first_name + ' ' + user.last_name)
				else:
					self.senders.append(user.first.name)

		self.messages.reverse()
		if self.obj.id != client.get_me().id:
			self.senders.reverse()

	def __repr__(self):
		return "id {} hash {} messages {} senders{}".format(self.id_, self.hash, self.messages, self.senders) 

@client.on(events.NewMessage)
async def new_message_event(event):
	try:
		chat_user_id = event.message.to_id.user_id
		endpoint_id = None
		sender = await event.get_sender()
		if chat_user_id == dia[-1].id_:
			endpoint_id = sender.id
		else : 
			endpoint_id = chat_user_id
	except:
		endpoint_id = -1
	for obj in dia:
		if obj.id_ == endpoint_id: 
=======
		for message in client.iter_messages(self.obj, limit = 10):
			self.messages.append(message.message)
		self.messages.reverse()

	def __repr__(self):
		return "id {} hash {} messages {}".format(self.id_, self.hash, self.messages)
 

@client.on(events.NewMessage)
async def new_message_event(event):
	sender = await event.get_sender()
	for obj in dia:
		if obj.id_ == sender.id: 
>>>>>>> e0599a6c8a6fb3af42d9bd8c8393ed44f387d3fb
			obj.messages.append(event.message.message)
			msg = obj.messages[-1]
			i = dia.index(obj) + 1 
	try:			
		print(msg)
	except:
		print('ошибка!!!')
	try:
		lock.acquire()
		queue.put((i,msg))
<<<<<<< HEAD
	except:
		pass 
=======
>>>>>>> e0599a6c8a6fb3af42d9bd8c8393ed44f387d3fb
	finally:
		lock.release()
	event_to_flask.set()
	event_to_async.wait()
	event_to_async.clear()
<<<<<<< HEAD


=======
	
>>>>>>> e0599a6c8a6fb3af42d9bd8c8393ed44f387d3fb
def resender_kek(): #no use in this one. Gonna keep it as a fun feature 
	#TODO integrate it in the working process 
	#TODO create a client func to activate this one 
	while True:
		sleep(5)
		d = datetime.now()
		socketio.emit('timer', {
		'data': str(d)
	}, namespace = '/main') 

def resender():
	while True:
		event_to_flask.wait()
		event_to_flask.clear()
		try:
			lock.acquire()
			id_, msg = queue.get()
		finally:
			lock.release()	
		socketio.emit('get_new_message', {
		'id': str(id_),
		'message': str(msg)
	}, namespace = '/main') 
<<<<<<< HEAD
		event_to_async.set()		
=======
		event_to_async.set()

		
>>>>>>> e0599a6c8a6fb3af42d9bd8c8393ed44f387d3fb

def start(client):	
	client.start()	
	logging.basicConfig(level=logging.ERROR)
	dia = getting_data(client)
	print(dia[-1].messages)
	return dia

def getting_data(client):
	dialogs = client.get_dialogs()	
	dia = []
	for ent in dialogs:
		try:
			if type(ent.entity) == User:
<<<<<<< HEAD
				#TODO get rid of botssssss (or better a special option for it ) or just mark them as bots 
				if ent.id == client.get_me().id:
					myself = dialog_(dia_obj =ent)
				else:
					obj = dialog_(dia_obj = ent)
=======
				#TODO get rid of botssssss (or better a special option for it )
				if ent.id == client.get_me().id:
					myself = dialog_(dia_obj =ent)
				else:
					obj = dialog_(dia_obj = ent )
>>>>>>> e0599a6c8a6fb3af42d9bd8c8393ed44f387d3fb
					dia.append(obj)		
		except:
			pass
	dia.append(myself)	
	return dia

<<<<<<< HEAD
dia = start(client)
=======
dia =start(client)
>>>>>>> e0599a6c8a6fb3af42d9bd8c8393ed44f387d3fb

 


		