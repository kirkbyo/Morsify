In this tutorial, we will be building a program where the text is inputted into a text file and we will convert the text inside the file to audible morse code.

### Requirements

- Raspberry Pi
- Internet Connection
- Python 2
- Headphones or Speakers

### Don’t reinvent the wheel
In this tutorial, we will be using other people’s code they have kindly open sourced or published online. The concept of not reinventing the wheel is commonly used when discussing programming and it’s important to understand. This concept indicates that there is no point writing every piece of your code yourself when someone else has already done the heavy lifting and wrote it. Although, not every piece of code you find online is written by some experienced programmer, so you must use your best judgment to tell if the code you found is efficient and makes sense to use in your program.

### What is a Raspberry Pi?
Raspberry Pi’s is a small, cheap computer that is very powerful. It runs it’s own OS called Raspbian and has tons of use cases. If you are interested in viewing some of the many uses cases for this amazing computer, follow this [link](http://www.itpro.co.uk/mobile/21862/raspberry-pi-top-21-projects-to-try-yourself).

### Setup the PI
We aren’t going to cover how to setup the Pi in this article, but if your Pi isn’t already setup you can follow this [article by Life Hacker](http://lifehacker.com/5976912/a-beginners-guide-to-diying-with-the-raspberry-pi).

### Downloading the necessary packages
For this project, we are going to need to download a package called `pyaudio`. This package allows us to play sounds on the Raspberry Pi. In order to download the package, we will be using `pip`. [Pip](https://en.wikipedia.org/wiki/Pip_(package_manager) is a package manager for Python, basically how it works other programmers publish there package on the platform which gives us access to download them and use it in are projects.

In order to download the package you need to open the command line; the command line allows you to control every aspect of your computer without a user interface. The command line looks like:
![Raspberry Pi Command line Icon](http://i.imgur.com/CNfNT7z.png)

Once you have the command line open, type the following command:
```
sudo pip install pyaudio
```
If needed the default password for the Pi is `raspberrypi`.

If the package successfully installed, you are ready to start!

### Beep Beep

It’s now time to start the actual implementation for this text to morse code generator. First thing first is to understand the problem at hand and how can we solve it.

**The problem:** Convert text from a `.txt` file to audible morse code.

Now that we understand are the problem we need to break it up into small steps that are easy to approach.

**Steps:**
1. Fetch the contents of the .txt file
2. Convert each individual character from the file to morse code.
3. Play the sound for the proper amount of time depending on the morse symbol.

#### 1. Fetching the contents from the .txt file.
The first thing we need to do is create a .txt file to actually read from. To do this we can use the `touch` command with the command line. `touch` allows us to create empty files using only the command line. To create a .txt file called output:
```
touch Desktop/output.txt
```
Now that we have a text file, we need to insert some text into it. Double click the file and type whatever you want the program to say.

Next, we need to create a python file called `main.py` to actually read the text in the file.
```
touch Desktop/main.py
```
In order to edit the `main.py` the file we need to use a text editor, the Pi comes built in with a notepad type app that we can use to edit the contents of the file. To edit the file using the command line, type
```
nano Desktop/main.py
```

Reading a file is simple in python, copy the following lines into the `main.py` file.

```python
# Name of the .txt file to be read
fileName = "output.txt"
# Finds the file matching the fileName and is within the same directory
fileObject = open(fileName, "r")
# Reads the file and removes any formatting
fileText = fileObject.read().rstrip()
# fileText contains a string of the text from .txt file.
```

Run the program with the command line. If nothing appears then you did everything right, if something appears under command you typed then there is an error somewhere in your code.
```python
python Desktop/main.py
```

#### 2. Convert each individual character from the file to morse code.

This logic wouldn’t be too hard to write ourselves, but would be a waste of time in my opinion because someone has already done this for us. Copy this code into its own file called `morse.py` or download the zip from [Gists](https://gist.github.com/kirkbyo/906ff2e6e85c7739e96bcc7daf84a6e9) and extract the zip onto your desktop.

**morse.py**
```python
# Morse Code logic provided from https://gist.github.com/ebuckley/1842461
class Morse:
    morseAlphabet = {
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        " " : "/"
    }

    #encode a message in morse code, spaces between words are represented by '/'
    def encode(self, message):
        encodedMessage = ""
        for char in message[:]:
            encodedMessage += self.morseAlphabet[char.upper()] + " "

        return encodedMessage
```

The code above assigns each character of the alphabet to its equivalent self in morse code symbols. The `encode` function converts strings to morse code and returns it in string format. Example:
```python
import morse

# morse is the name of the file
# Morse() initializes a new Morse() class
# encode("Hello world") passes a string of text and returns it's self in morse symbols.
encode = morse.Morse().encode(“Hello World”)
# Returns: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
```

Using this in are the project is now simple, all we have to do is import are `morse` file and convert the `fileText` to morse using the `encode` function provided by are `Morse` class.

```python
import morse

# Name of the .txt file to be read
fileName = "output.txt"
# Finds the file matching the fileName and is within the same directory
fileObject = open(fileName, "r")
# Reads the file and removes any formatting
fileText = fileObject.read().rstrip()
# fileText contains a string of the text from .txt file.

# Converts the text from .txt file to morse code
morseCode = morse.Morse().encode(fileText)
print(morseCode)
```

**What your project should look like at this point:** You should have a file called `morse.py` with the conversion logic and another file called `main.py` that contains the logic to open the file and then convert it to morse code. Running the file in the terminal should print the morse code equivalent to whatever the text is in your output.txt file.

```
python Desktop/main.py
```

#### 3. Making sounds

In order to use create are own custom sounds we will need to borrow some logic that [someone kindly already wrote](# http://askubuntu.com/questions/202355/how-to-play-a-fixed-frequency-sound-using-python) and use some libraries we have already installed on the system.

To start we need to define some variables for how the sound should play depending on what morse symbol it is. I highly encourage you to need through this [article](http://www.nu-ware.com/NuCode%20Help/index.html?morse_code_structure_and_timing_.htm) to get a better understanding of how morse code timing actually works.

```python
import morse

# Name of the .txt file to be read
fileName = "output.txt"
# Finds the file matching the fileName and is within the same directory
fileObject = open(fileName, "r")
# Reads the file and removes any formatting
fileText = fileObject.read().rstrip()
# fileText contains a string of the text from .txt file.

# Converts the text from .txt file to morse code
morseCode = morse.Morse().encode(fileText)
print(morseCode)

# MORSE Code Setup
dot = 1
dash = dot * 3
element_space = dot
letter_space = dot * 3
space = dot * 7
```

This where the code gets a little bit funky and possibly hard to understand, for now, it’s not essential to understand everything the following function is doing, other than the fact that when you call this function a sound gets created a plays for the amount of time you specified as the function parameter.

```python
from __future__ import division #Avoid division problems in Python 2
import morse
import math
import pyaudio
import time
import sys

# Name of the .txt file to be read
fileName = "output.txt"
# Finds the file matching the fileName and is within the same directory
fileObject = open(fileName, "r")
# Reads the file and removes any formatting
fileText = fileObject.read().rstrip()
# fileText contains a string of the text from .txt file.

# Converts the text from .txt file to morse code
morseCode = morse.Morse().encode(fileText)
print(morseCode)

# MORSE Code Setup
dot = 1
dash = dot * 3
element_space = dot
letter_space = dot * 3
space = dot * 7

# Creates and plays sound for the specified amount of time.
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

# Pauses the script at the end of each symbol to indicated the end of a symbol.
def elementPause():
    # Play beep.wav sound for element space
    time.sleep(element_space)
```

Last but not least we need to loop through each individual morse character and play the sound for the amount specified by are variables.

```python
# Loops through each character of the morse symbols.
for element in morseCode:
    if element == ".": # Plays sound for the dot
        playSound(dot)
        elementPause()
    elif element == "-": # Plays sound for the dash
        playSound(dash)
        elementPause()
    elif element == "/": # Plays sound for the element space (At the end of the word)
        playSound(space)
    elif element == " ": # Plays sound for the letter space (Between letters)
        playSound(letter_space)
    else:
        print("ERROR: Morse Symbol could not be found.")
        break
```


Your final `main.py` should resemble something as follows.

```python
from __future__ import division #Avoid division problems in Python 2
import morse
import math
import pyaudio
import time
import sys

# Name of the .txt file to be read
fileName = "output.txt"
# Finds the file matching the fileName and is within the same directory
fileObject = open(fileName, "r")
# Reads the file and removes any formatting
fileText = fileObject.read().rstrip()
# fileText contains a string of the text from .txt file.

# Converts the text from .txt file to morse code
morseCode = morse.Morse().encode(fileText)
print(morseCode)

# MORSE Code Setup
dot = 1
dash = dot * 3
element_space = dot
letter_space = dot * 3
space = dot * 7

# Creates and plays sound for the specified amount of time.
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

# Pauses the script at the end of each symbol to indicated the end of a symbol.
def elementPause():
    # Play beep.wav sound for element space
    time.sleep(element_space)

# Loops through each character of the morse symbols.
for element in morseCode:
    if element == ".": # Plays sound for the dot
        playSound(dot)
        elementPause()
    elif element == "-": # Plays sound for the dash
        playSound(dash)
        elementPause()
    elif element == "/": # Plays sound for the element space (At the end of the word)
        playSound(space)
    elif element == " ": # Plays sound for the letter space (Between letters)
        playSound(letter_space)
    else:
        print("ERROR: Morse Symbol could not be found.")
        break
```

Running the script should play morse code generated from your output.txt over your speakers or your headphones.

```
python Desktop/main.py
```

If everything is working, then congratulation you have just successfully built a text to morse code converter, enjoy communicating with your friends!
