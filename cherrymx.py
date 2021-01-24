import pygame
from pygame import mixer  # Load the popular external library
import time
from pynput.keyboard import Key, Listener

from tkinter import *
from tkinter import messagebox


pygame.mixer.pre_init(44100, -16, 1, 512)
mixer.init()

press = mixer.Sound('cherrymxclick.wav')
release = mixer.Sound('cherrymxrelease.wav')

press.set_volume(0.78)
release.set_volume(0.78)

char_states = []
for i in range(128): char_states.append(0)

def on_press(key):

    try:
        temp = ord('`')
        temp = ord(key.char)
    except AttributeError: pass

    if char_states[temp] == 0:
        mixer.find_channel().play(press)
        char_states[temp] = 1


def on_release(key):

    try:
        temp = ord('`')
        temp = ord(key.char)
    except AttributeError: pass

    if char_states[temp] == 1:
        mixer.find_channel().play(release)
        char_states[temp] = 0

    if key == Key.insert:
        # Stop listener
        return False
#sss
# Collect events until release
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()



