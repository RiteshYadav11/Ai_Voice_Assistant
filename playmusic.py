import pygame

def PlayMusic():
    pygame.mixer.init()
    pygame.mixer.music.load('path/to/music/file.mp3')
    pygame.mixer.music.play()
    return "Playing music"
