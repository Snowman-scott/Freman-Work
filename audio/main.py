import vlc
import time

audio = vlc.MediaPlayer("Scarlet Fire.mp3")  # File name should be "Scarlet Fire.mp3"
audio.play()  # No need to specify the file name again