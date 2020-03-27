from settings import *
from sprites import Sprites
from base import Base
from bird import Bird
from pipes import Pipes
from score import Score
from status import Status
from hitBoxe import HitBoxe
from drawer import Drawer
from audio import Audio

import pygame

def mainLoop(clock, window, sprites, audio):
    run = True
    status = Status.inMenu
    tick = 0

    drawer = Drawer(window)

    hitBoxe = HitBoxe(audio.hitSound, audio.dieSound, audio.pointSound)

    base = Base(sprites.base)
    bird = Bird(sprites.bird, audio.wingSound, hitBoxe)
    pipes = Pipes(sprites.pipe, hitBoxe)
    score = Score(sprites.numbers)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            if status == Status.inMenu and event.type == pygame.KEYUP and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                status = Status.inGame
            if status == Status.inGame and event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                bird.jump()
            if status == Status.inGameOver and event.type == pygame.KEYUP and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                status = Status.inMenu
                tick = 0
                base = Base(sprites.base)
                bird = Bird(sprites.bird, audio.wingSound, hitBoxe)
                pipes = Pipes(sprites.pipe, hitBoxe)
                score = Score(sprites.numbers)

        if status == Status.inGame:
            hitBase = hitBoxe.birdHitBase(bird, base)
            hitPipe = hitBoxe.birdHitPipes(bird, pipes)
            hitBoxe.birdPassPipe(bird, pipes.pipes, score)
            if hitBase or hitPipe:
                status = Status.inGameOver
                bird.die()

        if status == Status.inMenu:
            drawer.drawInMenu(sprites.background, sprites.message, base, bird, tick)
        elif status == Status.inGame:
            drawer.drawInGame(sprites.background, base, bird, pipes, score, tick)
        else:
            drawer.drawInGameOver(sprites.background, sprites.gameOver, base, bird, pipes, score, tick)

        if tick < FPS:
            tick += 1
        else:
            tick = 0

if __name__ == '__main__':
    pygame.init()

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption(GAMENAME)
    sprites = Sprites()
    audio = Audio()

    mainLoop(clock, window, sprites, audio)

    pygame.quit()
