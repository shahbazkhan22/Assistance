# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 02:41:32 2017

@author: shahb
"""

from gtts import gTTS
from playsound import playsound
import os
tts = gTTS(text="Welcome to Assistance", lang='en')
tts.save("welcome.mp3")
os.system("welcome.mp3")
playsound('C:/Users/shahb/Documents/Python Progs openCV/welcome.mp3')