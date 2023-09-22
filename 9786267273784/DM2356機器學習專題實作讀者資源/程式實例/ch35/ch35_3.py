# ch35_3.py
from gtts import gTTS
import pygame

text = "Hello, Machine Learning!"
tts = gTTS(text=text, lang='en')
tts.save("hello.mp3")

pygame.mixer.init()
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()



