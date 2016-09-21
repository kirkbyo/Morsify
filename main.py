from __future__ import division #Avoid division problems in Python 2
import morse
import math
import pyaudio
import time
import sys

# File Setup
fileName = "output.txt"
fileObject = open(fileName, "r")
fileText = fileObject.read().rstrip()

morseCode = morse.Morse().encode(fileText)

# MORSE Code Setup
dot = 1
dash = dot * 3
element_space = dot
letter_space = dot * 3
space = dot * 7


"""Plays sound for specified amount of time.
@param time: Int for how long the sound plays for

Logic provided from:
http://askubuntu.com/questions/202355/how-to-play-a-fixed-frequency-sound-using-python
"""
def playSound(time):
    PyAudio = pyaudio.PyAudio
    RATE = 10000
    WAVE = 1000
    data = ''.join([chr(int(math.sin(x/((RATE/WAVE)/math.pi))*127+128)) for x in xrange(RATE)])
    p = PyAudio()

    stream = p.open(format =
                    p.get_format_from_width(1),
                    channels = 1,
                    rate = RATE,
                    output = True)
    for DISCARD in xrange(time):
        stream.write(data)
    stream.stop_stream()
    stream.close()
    p.terminate()

# Loops through each character of the morse symbols.
for element in morseCode:
    if element == ".": # Plays sound for the dot
        playSound(dot)
        time.sleep(element_space)
    elif element == "-": # Plays sound for the dash
        playSound(dash)
        time.sleep(element_space)
    elif element == "/": # Plays sound for the element space (At the end of the word)
        playSound(space)
    elif element == " ": # Plays sound for the letter space (Between letters)
        playSound(letter_space)
    else: # Symbol not found
        print("ERROR: Morse Symbol could not be found.")
        break
