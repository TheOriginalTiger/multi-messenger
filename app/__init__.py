from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app, async_mode='threading')

from app import tg_info, threads

client = threads.client
tg = threads.tg

lock = threads.lock # all the threading stuff
event_to_flask = threads.event_to_flask
event_to_async = threads.event_to_async
queue = threads.queue


from app import  tg_module, routes,  templates

tg.start()

