from pygame import mixer
mixer.init()
mixer.music.load("deathbed.mp3")
mixer.music.play()
put = input("change")
while True:
    if(put == " "):
        mixer.music.stop()
        mixer.music.load("staywithme.mp3")
        mixer.music.play()
        put = input("change")
        if(put == " "):
            break
