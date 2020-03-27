import pygame

class Drawer:

    def __init__(self, window):
        self.window = window

    def drawInMenu(self, background, message, base, bird, tick):
        self.window.blit(background.image, (background.x, background.y))
        self.window.blit(message.image, (message.x, message.y))
        base.drawInGame(self.window)
        bird.drawInMenu(self.window, tick)
        pygame.display.update()

    def drawInGame(self, background, base, bird, pipes, score, tick):
        self.window.blit(background.image, (background.x, background.y))
        pipes.drawInGame(self.window)
        base.drawInGame(self.window)
        score.draw(self.window)
        bird.drawInGame(self.window, base.sprite.y, tick)
        pygame.display.update()

    def drawInGameOver(self, background, gameOver, base, bird, pipes, score, tick):
        self.window.blit(background.image, (background.x, background.y))
        pipes.drawInGameOver(self.window)
        base.drawInGameOver(self.window)
        score.draw(self.window)
        self.window.blit(gameOver.image, (gameOver.x, gameOver.y))
        bird.drawInGame(self.window, base.sprite.y, tick)
        pygame.display.update()
