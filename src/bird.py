from settings import FPS

import pygame

YMAXINMENU = 240
YMININMENU = 230

FLAPPERSECOND = 5
RAISEPERSECOND = 2

JUMPVELOCITY = 4
FALLVELOCITY = 3
DECELERATIONPERSECOND = 10
JUMPTIMEOUT = 15

BASICROTATION = 20
MAXROTATION = -90
ROTATIONVELOCITY = 3

class Bird:

    def __init__(self, sprites, wingSound, hitBoxe):
        self.sprites = sprites
        self.wingSound = wingSound
        self.x = self.sprites[0].x
        self.y = self.sprites[0].y
        self.hitMask = hitBoxe.getHitMask(self.sprites[0].image, self.sprites[0].width, self.sprites[0].height)

        self.flapCount = 0
        self.yRaise = 1

        self.jumpTime = 0
        self.jumped = False
        self.jumping = False
        self.vY = JUMPVELOCITY
        self.rotate = 0
        self.isDead = False

    def _flap(self, tick):
        if tick != 0 and tick % FLAPPERSECOND == 0 and self.flapCount < 3:
            self.flapCount += 1
        elif tick != 0 and tick % FLAPPERSECOND == 0:
            self.flapCount = 0

    def _raise(self, tick):
        if tick != 0 and tick % RAISEPERSECOND == 0:
            self.y += self.yRaise
        if self.y == YMAXINMENU:
            self.yRaise = -1
        elif self.y == YMININMENU:
            self.yRaise = 1

    def jump(self):
        self.wingSound.play()
        self.jumpTime = 0
        self.jumped = True
        self.jumping = True

    def die(self):
        self.isDead = True

    def drawInMenu(self, window, tick):
        window.blit(self.sprites[self.flapCount].image, (self.x, self.y))
        self._flap(tick)
        self._raise(tick)

    def drawInGame(self, window, baseY, tick):
        window.blit(pygame.transform.rotate(self.sprites[self.flapCount].image, self.rotate), (self.x, self.y))

        if self.isDead == False:
            self._flap(tick)

        if self.jumping:
            self.jumpTime += 1

        if self.y + self.sprites[0].height < baseY:
            if self.jumping == False:
                self.y = self.y + FALLVELOCITY
                if self.rotate > MAXROTATION:
                    self.rotate -= ROTATIONVELOCITY
            else:
                if self.y > -self.sprites[0].height:
                    self.y += -self.vY
                if self.jumpTime % DECELERATIONPERSECOND == 0:
                    self.vY -= 1

            if self.jumping == True and self.jumpTime >= JUMPTIMEOUT:
                self.jumpTime = 0
                self.jumping = False
                self.vY = JUMPVELOCITY

        if self.jumped:
            self.jumped = False
            self.rotate = BASICROTATION
