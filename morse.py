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
