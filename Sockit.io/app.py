from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    send(msg, broadcast=True)

@socketio.on('user_connected')
def handle_user_connected(data):
    username = data['username']
    print(f"User connected: {username}")
    send(f"{username} has connected", broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    print("User disconnected")
    send("A user has disconnected", broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
