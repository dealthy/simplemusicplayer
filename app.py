from pygame import mixer
from os import walk
import random
import threading

def getsong(playlist):
    song = []
    for (dirpath, dirnames, filenames) in walk([playlist]):
        song.extend(filenames)
        break
    
    for i in range(len(song)):
        temp = song[i]
        if( temp[0] == "." ):
            del song[i]

    return song


def shuffle(songlist):
    shufflelist = []

    for i in range(len(songlist)):
        randomnum = random.randint(1,len(songlist)) - 1
        shufflelist.append(songlist[randomnum])
        del songlist[randomnum]

    return shufflelist

def playback():
    mixer.music.stop()
    mixer.music.load(shufflelist[i])
    mixer.music.play()

mixer.init()

shufflelist = shuffle(getsong("work"))
status = "work"
mixer.music.set_volume(0.6)

for i in range(len(shufflelist)):

    playback()

    while True:

        print("p = pause; r = resume; e = exit; m = mute; s = switch")
        query = input(">>> ")

        if query == "p":
            mixer.music.pause()
        elif query == "r":
            mixer.music.unpause()
        elif query == "e":
            mixer.music.stop()
            break
        elif query == "m":
            if(mixer.music.get_volume == 0.6):
                mixer.music.set_volume(0)
            else:
                mixer.music.set_volume(0.6)
        elif query == "s":
            if(status == "work"):
                shufflist = shuffle(getsong("chill"))
                status = "chill"
                playback()
            else:
                shuffelist = shuffle(getsong("work"))
                status = "work"
                playback()
        else:
            print("syntax error")