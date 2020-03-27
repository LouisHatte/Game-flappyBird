import sys
import pygame

class Audio:

    def __init__(self):
        if 'win' in sys.platform:
            extension = '.wav'
        else:
            extension = '.ogg'

        self.dieSound = pygame.mixer.Sound('../assets/audio/die' + extension)
        self.hitSound = pygame.mixer.Sound('../assets/audio/hit' + extension)
        self.pointSound = pygame.mixer.Sound('../assets/audio/point' + extension)
        self.wingSound = pygame.mixer.Sound('../assets/audio/wing' + extension)
