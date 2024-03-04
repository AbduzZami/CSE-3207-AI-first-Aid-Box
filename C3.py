import pyaudio
import wave
import threading
import tkinter as tk
import speech_recognition as sr

# the file name output you want to record into
filename = "recorded.wav"
# set the chunk size of 1024 samples
chunk = 1024
# sample format
FORMAT = pyaudio.paInt16
# mono, change to 2 if you want stereo
channels = 1
# 44100 samples per second
sample_rate = 44100
# initialize PyAudio object
p = pyaudio.PyAudio()

# global recording flag
is_recording = False

def start_recording():
    global is_recording
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    is_recording = True
    print("Recording...")
    while is_recording:
        data = stream.read(chunk)
        frames.append(data)
    print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(sample_rate)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()
    # convert audio to text
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        text_area.insert(tk.END, text)

def stop_recording():
    global is_recording
    is_recording = False

# create a tkinter window
root = tk.Tk()
root.geometry('800x600')  # set window size

# create start and stop buttons
start_button = tk.Button(root, text='Start', command=lambda: threading.Thread(target=start_recording).start())
stop_button = tk.Button(root, text='Stop', command=stop_recording)

# place the buttons
start_button.pack()
stop_button.pack()

# create a text area for the transcript
text_area = tk.Text(root)
text_area.pack()

# run the tkinter event loop
root.mainloop()

# terminate pyaudio object
p.terminate()
