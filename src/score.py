from settings import WINDOWWIDTH

import pygame

class Score:

    def __init__(self, sprites):
        self.sprites = sprites
        self.score = 0

    def incrementScore(self):
        if self.score < 9999:
            self.score += 1

    def draw(self, window):
        digits = [int(digit) for digit in list(str(self.score))]
        totalDigitsWidth = sum([self.sprites[digit].width for digit in digits])
        xShift = (WINDOWWIDTH - totalDigitsWidth) / 2

        for digit in digits:
            window.blit(self.sprites[digit].image, (xShift, self.sprites[0].y))
            xShift += self.sprites[digit].width
