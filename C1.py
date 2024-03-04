import serial
import time
import requests


import tkinter as tk
import speech_recognition as sr

import main

# Set the Arduino serial port (update with your port)
arduino_port = "/dev/ttyACM0"  # Linux example, for Windows use something like "COM3"

# Set the API endpoint
api_url = "https://example.com/get_sequence"

# Open a serial connection to Arduino
ser = serial.Serial(arduino_port, 9600, timeout=1)

response = [
    {
    'drawer_no':1,
    'instruction':"take the antiseptic and rub it in the wounded area.",
    },
    {
    'drawer_no':2,
    'instruction':"take the bandage and use it on the wounded area.",
    },
    {
    'drawer_no':1,
    'instruction':"take the antiseptic and rub it in the wounded area.",
    },
    {
    'drawer_no':3,
    'instruction':"take the bandage and use it on the wounded area.",
    },
    {
    'drawer_no':4,
    'instruction':"take the antiseptic and rub it in the wounded area.",
    },
    {
    'drawer_no':2,
    'instruction':"take the bandage and use it on the wounded area.",
    }
]


def create_gui(input_text):
    global label
    root = tk.Tk()
    root.geometry('800x600')
    
    # Use a Label instead of Text
    label = tk.Label(root, text=input_text, font=("Helvetica", 24))  # Adjust the font size as needed
    label.pack(padx=20, pady=20)
    
    root.after(2000, root.destroy)
    root.mainloop()

def get_sequence_from_api():
    # Make a request to the API to get the sequence
    # response = requests.get(api_url)
    # return response.text.strip()

    return response


def send_to_arduino(item):
    # Send the integer to Arduino
    ser.write(str(item).encode() + b'\n')

    



    # Wait for the Arduino to process the item
    time.sleep(2)  # Adjust as needed

try:
    # Get the sequence from the API
    sequence = get_sequence_from_api()

    for item in sequence:
        # Send each item to Arduino
        print(f"Sending {item['drawer_no']} to Arduino" )
        send_to_arduino(item['drawer_no'])
        # create a window and print a text message and generate text to audio, like reverse of the main.py
        create_gui(item['instruction'])

except KeyboardInterrupt:
    print("Script terminated by user.")
    # break
except Exception as e:
    print(f"Error: {e}")
    time.sleep(5)  # Wait before retrying
