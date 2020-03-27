from status import Status

import pygame

class HitBoxe:

    def __init__(self, hitSound, dieSound, pointSound):
        self.hitSound = hitSound
        self.dieSound = dieSound
        self.pointSound = pointSound

    def _isPixelCollision(self, hitBoxe1, hitBoxe2, hitMask1, hitMask2):
        hitBoxe = hitBoxe1.clip(hitBoxe2)

        if hitBoxe.width * hitBoxe.height == 0:
            return False

        x1, y1 = hitBoxe.x - hitBoxe1.x, hitBoxe.y - hitBoxe1.y
        x2, y2 = hitBoxe.x - hitBoxe2.x, hitBoxe.y - hitBoxe2.y

        for x in range(hitBoxe.width):
            for y in range(hitBoxe.height):
                if hitMask1[x1 + x][y1 + y] and hitMask2[x2 + x][y2 + y]:
                    return True
        return False

    def getHitMask(self, image, width, height):
        mask = []
        for x in range(width):
            mask.append([])
            for y in range(height):
                isTransparent = bool(image.get_at((x,y))[3])
                mask[x].append(isTransparent)
        return mask

    def birdHitBase(self, bird, base):
        if bird.y + bird.sprites[0].height >= base.sprite.y:
            self.hitSound.play()
            self.dieSound.play()
            return True
        return False

    def birdPassPipe(self, bird, pipes, score):
        for pairPipe in pipes:
            if pairPipe.passed == False and bird.x > pairPipe.x + pairPipe.sprite.width / 2:
                self.pointSound.play()
                score.incrementScore()
                pairPipe.passed = True

    def birdHitPipes(self, bird, pipes):
        birdHitBoxe = pygame.Rect(bird.x, bird.y, bird.sprites[0].width, bird.sprites[0].height)

        for pairPipe in pipes.pipes:
            upPipeHitBoxe = pygame.Rect(pairPipe.x, pairPipe.yDown, pairPipe.sprite.width, pairPipe.sprite.height)
            bottomPipeHitBoxe = pygame.Rect(pairPipe.x, pairPipe.yUp, pairPipe.sprite.width, pairPipe.sprite.height)

            isUpCollision = self._isPixelCollision(birdHitBoxe, upPipeHitBoxe, bird.hitMask, pipes.upHitMask)
            isBottomCollision = self._isPixelCollision(birdHitBoxe, bottomPipeHitBoxe, bird.hitMask, pipes.bottomHitMask)

            if isUpCollision or isBottomCollision:
                self.hitSound.play()
                self.dieSound.play()
                return True
        return False
