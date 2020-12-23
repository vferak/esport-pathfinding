import pygame


class Banner:
    """
    Banner for persons - Satyrs or Hero. A banner shows the score of the person
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load('banner/banner.png')

    def show(self, game_display):
        game_display.blit(self.img, (self.x, self.y))

class Person:
    pass