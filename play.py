# -*- coding:utf-8 -*-

import time
import pygame
from mutagen.mp3 import MP3


def play():
    times = MP3(r'/home/pi/audio.mp3').info.length
    pygame.mixer.init()
    pygame.mixer.music.load(r'/home/pi/audio.mp3')
    pygame.mixer.music.play()
    print '播放中...'
    time.sleep(times)
    pygame.mixer.music.stop()

