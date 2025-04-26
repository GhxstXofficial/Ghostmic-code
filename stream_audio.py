import socketio
import sounddevice as sd
import numpy as np
import threading
import time

sio = socketio.Client()
sio.connect('http://localhost:5000')

samplerate = 16000
blocksize = 1024

def callback(indata, frames, time, status):
    audio_chunk = indata.copy().tobytes()
    sio.emit('audio_stream', audio_chunk)

def stream():
    with sd.InputStream(callback=callback, channels=1, samplerate=samplerate, blocksize=blocksize):
        while True:
            time.sleep(0.1)

if __name__ == '__main__':
    stream()
