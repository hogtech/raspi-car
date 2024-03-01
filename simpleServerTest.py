from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from servoController import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'justasecretkeythatishouldputhere'
socketio = SocketIO(app)

@socketio.on('connect')
def test_connect():
    print('Client connected')
    testServo()
    emit('response', {'message': 'Hello from Flask server!'})

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
