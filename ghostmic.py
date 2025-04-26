from flask import Flask, render_template, send_file
from flask_socketio import SocketIO
import threading
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    if os.path.exists('recordings/recording.wav'):
        return send_file('recordings/recording.wav', as_attachment=True)
    return "Recording not found", 404

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
