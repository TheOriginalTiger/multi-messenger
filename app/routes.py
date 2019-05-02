from app import app, socketio, lock, client
from flask import render_template
from app import tg_module, threads,tg_info
from flask_socketio import emit
from threading import Lock
from queue import Queue
from telethon import TelegramClient, sync, events, connection
import random


thread = None
locky = Lock()
id_queue = Queue()

@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html', title= 'main')	

@app.route('/dialogs')
def dialogs():
	dia = tg_module.dia
	return render_template(
        'dialogs.html', 
        title = 'dialogs', 
        dias = dia, 
        amount = range(len(dia)) 
    )

@socketio.on('connect', namespace='/main')
def test_connect():
    global thread
    #TODO change the idea of sending the user's name 
    name = tg_module.dia[-1].obj.name 
    socketio.emit('info_responder', {'self_name': name}, namespace = '/main')
    with locky:
        if thread is None:
            thread = socketio.start_background_task(target = tg_module.resender)

@app.route('/dialog/<id_>')    
def dialog(id_):

    senders = tg_module.dia[int(id_)].senders
    messages = tg_module.dia[int(id_)].messages
    name = tg_module.dia[int(id_)].name
    return render_template(
        "dialog_page.html", 
        senders = senders, 
        messages = messages, 
        amount = range(len(messages)), 
        name = name
    )

@socketio.on('get_message', namespace = '/main')
def get_message(messaga):
    print(messaga)    
    msg = messaga['messaga'].encode('l1').decode()
    threads.one_more_queue.put((tg_module.dia[int(messaga['user_id'])].obj, msg))
    r = threads.message_sender()
    r.start()
    