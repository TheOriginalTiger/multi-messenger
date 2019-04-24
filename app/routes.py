from app import app, socketio, lock
from flask import render_template
from app import tg_module
from flask_socketio import emit
from threading import Lock


thread = None
locky = Lock()


@app.route('/')
@app.route('/main')
def main():
	return render_template('main.html', title = 'main')
	

@app.route('/dialogs')
def dialogs():
	dia = tg_module.dia
	return render_template('dialogs.html', title = 'dialogs', dias = dia, amount = range(len(dia)) )

@socketio.on('connect', namespace='/main')
def test_connect():
    global thread
    with locky:
        if thread is None:
            thread = socketio.start_background_task(target = tg_module.resender)
    
