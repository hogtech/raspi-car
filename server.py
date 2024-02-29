# server.py
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    socketio.emit('response', 'Message received: ' + message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
