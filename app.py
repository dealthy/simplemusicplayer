from pygame import mixer
mixer.init()

mixer.music.load("song.mp3")
mixer.music.set_volume(1.2)
mixer.music.play()

while True:
    print("p = pause; r = resume; e = exit")
    query = input(">>> ")
    if query == "p":
        mixer.music.pause()
    elif query == "r":
        mixer.music.unpause()
    elif query == "e":
        mixer.music.stop()
        break
    else:
        print("syntax error")